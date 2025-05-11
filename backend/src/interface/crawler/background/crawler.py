import requests
import time
import threading

from . import exc
from .parser import IAMActionHTMLParser, ServiceLinkHTMLParser

from src.usecase.document_site import IDocumentSiteUseCase

CRAWL_URL = "https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html"


class Crawler:
    def __init__(
        self, usecase: IDocumentSiteUseCase, crawler_stop_event: threading.Event
    ):
        self.crawler_stop_event = crawler_stop_event
        self.usecase = usecase

    def run(self):
        while not self.crawler_stop_event.is_set():
            all_actions = self.crawl_all_service_actions()

            for _ in range(86400):
                if self.crawler_stop_event.is_set():
                    break
                time.sleep(1)

    def extract_side_nav_links(self):
        try:
            content = self.usecase.get_document_top_site()
            print(content)
            parser = ServiceLinkHTMLParser()
            parser.feed(content.content)
            links = list(parser.links)
            print(f"[INFO] サイドナビのlink_ページリンク数: {len(links)}")
            return links
        except Exception as e:
            print(f"[ERROR] サイドナビページリンク抽出失敗: {e}")
            return []

    def crawl_all_service_actions(self):
        links = self.extract_side_nav_links()
        all_actions = {}
        for link in links[:3]:
            actions = self.crawl_service_action_page(link)
            all_actions[link] = actions
            # セキュリティ・負荷対策: 1秒待機
            time.sleep(1)
        return all_actions

    def crawl_service_action_page(self, service_url):
        base_url = "https://docs.aws.amazon.com/service-authorization/latest/reference/"
        full_url = (
            base_url + service_url[len("reference/") :]
            if service_url.startswith("reference/")
            else base_url + service_url
        )
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
            print(
                f"[ERROR] サービスアクションページ({service_url})のクローリング失敗: {e}"
            )
            return []


class CrawlerHandler:
    def __init__(self, usecase: IDocumentSiteUseCase):
        self.crawler_thread = None
        self.crawler_stop_event = threading.Event()
        self.usecase = usecase

    def start(self):
        if self.crawler_thread and self.crawler_thread.is_alive():
            raise exc.AlreadyCrawlerRunningException()
        self.crawler_stop_event.clear()
        crawler = Crawler(
            usecase=self.usecase,
            crawler_stop_event=self.crawler_stop_event,
        )
        self.crawler_thread = threading.Thread(target=crawler.run, daemon=True)
        self.crawler_thread.start()

    def stop(self):
        if not self.crawler_thread or not self.crawler_thread.is_alive():
            raise exc.NotRunningCrawlerException()
        self.crawler_stop_event.set()
        self.crawler_thread.join()

    def get_status(self):
        return self.crawler_thread is not None and self.crawler_thread.is_alive()
