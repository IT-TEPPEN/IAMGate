from fastapi import APIRouter, HTTPException

from ..background import CrawlerHandler, exc

from src.usecase.document_site import IDocumentSiteUseCase


def setup_crawler_router(crawlerHandler: CrawlerHandler) -> APIRouter:
    """
    Set up the crawler handler with the provided use case.

    :param usecase: The use case to be used by the crawler handler.
    """
    router = APIRouter()

    @router.get("/crawler-status")
    def crawler_status():
        return {"running": crawlerHandler.get_status()}

    return router
