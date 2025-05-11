from fastapi import APIRouter, HTTPException

from ..background import CrawlerHandler, exc

from src.usecase.document_site import IDocumentSiteUseCase


def setup_crawler_router(usecase: IDocumentSiteUseCase):
    """
    Set up the crawler handler with the provided use case.

    :param usecase: The use case to be used by the crawler handler.
    """
    router = APIRouter()

    crawlerHandler = CrawlerHandler(usecase)

    @router.post("/start-crawler")
    def start_background_crawler():
        try:
            crawlerHandler.start()
            return {"status": "started"}
        except exc.AlreadyCrawlerRunningException as e:
            raise HTTPException(
                status_code=400, detail="Crawler already running"
            ) from e

    @router.post("/stop-crawler")
    def stop_background_crawler():
        try:
            crawlerHandler.stop()
            return {"status": "stopped"}
        except exc.NotRunningCrawlerException as e:
            raise HTTPException(status_code=400, detail="Crawler not running") from e

    @router.get("/crawler-status")
    def crawler_status():
        return {"running": crawlerHandler.get_status()}

    return router
