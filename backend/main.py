from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from src.interface.crawler.api import setup_crawler_router
from src.infrastructure import setup_infrastructure
from src.infrastructure.share.connection import get_engine
from sqlmodel import SQLModel

from src.usecase.document_site import DocumentSiteUseCase
from src.interface.crawler.background import CrawlerHandler


def create_db_and_tables():
    SQLModel.metadata.create_all(get_engine())


def setup() -> FastAPI:
    """
    Setup the FastAPI application.
    """

    infra = setup_infrastructure()
    usecase = DocumentSiteUseCase(
        document_site_repository=infra.document_site_repository,
        document_site_adapter=infra.document_site_adapter,
    )
    crawlerHandler = CrawlerHandler(usecase)

    # lifespanイベントハンドラでDB初期化
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        create_db_and_tables()

        crawlerHandler.start()

        yield

    # Create the FastAPI application
    app = FastAPI(lifespan=lifespan)
    router_v1 = APIRouter()

    setup_crawler_router(router_v1, crawlerHandler, usecase)

    # Include routers
    app.include_router(router_v1, prefix="/api/v1", tags=["v1"])

    return app


app = setup()
