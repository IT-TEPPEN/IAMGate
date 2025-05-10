from fastapi import FastAPI, HTTPException
import threading
import time
import requests
from html.parser import HTMLParser

app = FastAPI()

crawler_thread = None
crawler_stop_event = threading.Event()

CRAWL_URL = "https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html"

class IAMActionHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.current_row = []
        self.rows = []
        self.cell_data = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.in_table = True
        if self.in_table and tag == 'tr':
            self.in_row = True
            self.current_row = []
        if self.in_row and tag == 'td':
            self.in_cell = True
            self.cell_data = ''

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
        if tag == 'tr' and self.in_row:
            self.in_row = False
            if self.current_row:
                self.rows.append(self.current_row)
        if tag == 'td' and self.in_cell:
            self.in_cell = False
            self.current_row.append(self.cell_data.strip())

    def handle_data(self, data):
        if self.in_cell:
            self.cell_data += data

class ServiceLinkHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.in_a = False
        self.current_href = None

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.in_table = True
        if self.in_table and tag == 'tr':
            self.in_row = True
        if self.in_row and tag == 'td':
            self.in_cell = True
        if self.in_cell and tag == 'a':
            self.in_a = True
            for attr in attrs:
                if attr[0] == 'href' and attr[1].startswith('reference/services/'):
                    self.current_href = attr[1]

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
        if tag == 'tr':
            self.in_row = False
        if tag == 'td':
            self.in_cell = False
        if tag == 'a':
            self.in_a = False
            self.current_href = None

    def handle_data(self, data):
        if self.in_a and self.current_href:
            self.links.append(self.current_href)
            self.current_href = None

class SideNavLinkHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(f"[DEBUG] nav内aタグhref: {attr[1]}")
                if attr[0] == 'href' and attr[1].startswith('./list_'):
                    self.links.add(attr[1])

    def handle_endtag(self, tag):
        pass

def extract_side_nav_links():
    try:
        resp = requests.get(CRAWL_URL, timeout=10)
        resp.raise_for_status()
        parser = SideNavLinkHTMLParser()
        parser.feed(resp.text)
        links = list(parser.links)
        print(f"[INFO] サイドナビのlink_ページリンク数: {len(links)}")
        return links
    except Exception as e:
        print(f"[ERROR] サイドナビページリンク抽出失敗: {e}")
        return []

def extract_service_action_links():
    try:
        resp = requests.get(CRAWL_URL, timeout=10)
        resp.raise_for_status()
        parser = ServiceLinkHTMLParser()
        parser.feed(resp.text)
        # 重複除去
        links = list(set(parser.links))
        print(f"[INFO] サービスアクションページリンク数: {len(links)}")
        return links
    except Exception as e:
        print(f"[ERROR] サービスアクションページリンク抽出失敗: {e}")
        return []

def crawl_service_action_page(service_url):
    base_url = "https://docs.aws.amazon.com/service-authorization/latest/reference/"
    full_url = base_url + service_url[len("reference/"):] if service_url.startswith("reference/") else base_url + service_url
    try:
        resp = requests.get(full_url, timeout=10)
        resp.raise_for_status()
        parser = IAMActionHTMLParser()
        parser.feed(resp.text)
        # 例: 最初の3件だけ出力
        for row in parser.rows[:3]:
            print(f"[SERVICE PAGE] {service_url} : {row}")
        return parser.rows
    except Exception as e:
        print(f"[ERROR] サービスアクションページ({service_url})のクローリング失敗: {e}")
        return []

def crawl_all_service_actions():
    links = extract_side_nav_links()
    all_actions = {}
    for link in links:
        actions = crawl_service_action_page(link)
        all_actions[link] = actions
        # セキュリティ・負荷対策: 1秒待機
        time.sleep(1)
    return all_actions

def crawl_iam_actions():
    try:
        resp = requests.get(CRAWL_URL, timeout=10)
        resp.raise_for_status()
        parser = IAMActionHTMLParser()
        parser.feed(resp.text)
        # 例: 最初の5件だけ出力
        for row in parser.rows[:5]:
            print(row)
        return parser.rows
    except Exception as e:
        print(f"[ERROR] IAMアクションのクローリング失敗: {e}")
        return []

def crawler():
    while not crawler_stop_event.is_set():
        all_actions = crawl_all_service_actions()
        # TODO: DB保存処理をここに追加
        time.sleep(86400)  # 24時間ごと

@app.post("/start-crawler")
def start_crawler():
    global crawler_thread
    if crawler_thread and crawler_thread.is_alive():
        raise HTTPException(status_code=400, detail="Crawler already running")
    crawler_stop_event.clear()
    crawler_thread = threading.Thread(target=crawler, daemon=True)
    crawler_thread.start()
    return {"status": "started"}

@app.post("/stop-crawler")
def stop_crawler():
    if not crawler_thread or not crawler_thread.is_alive():
        raise HTTPException(status_code=400, detail="Crawler not running")
    crawler_stop_event.set()
    crawler_thread.join()
    return {"status": "stopped"}

@app.get("/crawler-status")
def crawler_status():
    running = crawler_thread is not None and crawler_thread.is_alive()
    return {"running": running}