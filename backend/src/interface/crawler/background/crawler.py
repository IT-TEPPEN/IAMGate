import requests
import time
import threading

from . import exc
from .parser import IAMActionHTMLParser, ServiceLinkHTMLParser

from src.usecase.document_site import IDocumentSiteUseCase

CRAWL_URL = "https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html"


class Crawler:
    def __init__(self, usecase: IDocumentSiteUseCase):
        self.usecase = usecase

    def run(self):
        while True:
            try:
                self.usecase.update_actions_list_page_properties()
            except Exception as e:
                print(f"[ERROR] クローリング処理で例外1: {e}")

            for i in range(1440):
                try:
                    with self.usecase.get_actions_list_page_property_crawling() as site_property:
                        if site_property is None:
                            print("[INFO] クローリング対象は存在しません。")
                        else:
                            print(f"[INFO] クローリング対象: {site_property.url}")
                            self.crawl_service_action_page(site_property.url)
                except Exception as e:
                    print(f"[ERROR] クローリング処理で例外2: {e}")
                finally:
                    time.sleep(5)

    def crawl_service_action_page(self, service_url: str):
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
        self.usecase = usecase

    def start(self):
        if self.crawler_thread and self.crawler_thread.is_alive():
            raise exc.AlreadyCrawlerRunningException()
        crawler = Crawler(
            usecase=self.usecase,
        )
        self.crawler_thread = threading.Thread(target=crawler.run, daemon=True)
        self.crawler_thread.start()

    def get_status(self):
        return self.crawler_thread is not None and self.crawler_thread.is_alive()
