import time
import threading

from . import exc

from src.usecase.document_site import IDocumentSiteUseCase


class Crawler:
    def __init__(self, usecase: IDocumentSiteUseCase):
        self.usecase = usecase

    def run(self):
        while True:
            try:
                self.usecase.update_actions_list_page_properties()
            except Exception as e:
                print(f"[ERROR] クローリング処理で例外1: {e}")

            try:
                with self.usecase.get_actions_list_page_property_crawling() as site_property:
                    if site_property is None:
                        print("[INFO] クローリング対象は存在しません。")
                    else:
                        print(f"[INFO] クローリング対象: {site_property.url}")

                        content = self.usecase.crawl_actions_list_page(
                            actions_list_page_property=site_property
                        )
                        service_actions = self.usecase.get_service_actions_from_content(
                            content.content
                        )

                        print(f"[INFO] Service Name   : {service_actions.service_name}")
                        print(f"[INFO] Service Prefix : {service_actions.id}")
                        print(
                            f"[INFO] Service Actions: {len(service_actions.service_actions)}"
                        )
                        for action in service_actions.service_actions[:10]:
                            print(f"[INFO] Action Code: {action.id}")
                            print(f"[INFO] Action Name: {action.action_name}")
                            print(f"[INFO] Action URL : {action.action_url}")
                            print(f"[INFO] Description: {action.description}")
                            print(f"[INFO] Access Level: {action.access_level}")
            except Exception as e:
                print(f"[ERROR] クローリング処理で例外2: {e}")
            finally:
                time.sleep(10)


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
