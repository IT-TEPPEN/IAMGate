from fastapi import APIRouter, HTTPException

from ..background import CrawlerHandler
from src.usecase.document_site import IDocumentSiteUseCase, dto, exc


def setup_crawler_router(
    parent_router: APIRouter,
    crawlerHandler: CrawlerHandler,
    usecase: IDocumentSiteUseCase,
) -> APIRouter:
    """
    Set up the crawler handler with the provided use case.

    :param usecase: The use case to be used by the crawler handler.
    """
    status_router = APIRouter(prefix="/crawler-status")
    target_router = APIRouter(prefix="/crawler-targets")

    @status_router.get("")
    def crawler_status():
        return {"running": crawlerHandler.get_status()}

    @target_router.get("")
    def crawler_targets():
        pages = usecase.list_actions_pages()
        return {"page_count": len(pages), "targets": pages}

    @target_router.get("/{document_id}")
    def crawler_target(document_id: str):
        target = usecase.get_crawling_target(document_id=document_id)

        if target is None:
            raise HTTPException(status_code=404, detail="Target not found")

        return target

    @target_router.put("/{document_id}")
    def crawler_target_update(document_id: str):
        try:
            target = usecase.add_crawling_target(
                dto.AddCrawlingTargetRequest(site_id=document_id, crawl_interval=10)
            )

            return target
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail="Target not found")

    @target_router.delete("/{document_id}")
    def crawler_target_delete(document_id: str):
        try:
            usecase.delete_crawling_target(document_id=document_id)
            return {"message": "Deleted the target."}
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail="Target not found")

    # @target_router.delete("")
    # def crawler_targets_delete():
    #     usecase.clear_actions_pages()
    #     return {"message": "Deleted all action list page properties."}

    parent_router.include_router(target_router)
    parent_router.include_router(status_router)
