from .interface import Infrastructure
from .postgresql import setup_postgresql_infrastructure
from ..site.adapter import DocumentSiteAdapter
from src.environment import DB_TYPE


__all__ = [
    "setup_infrastructure",
]


def setup_infrastructure() -> Infrastructure:
    """
    Setup the infrastructure for the application.
    """
    db_type = DB_TYPE

    if db_type is None:
        print("DB_TYPE is not set. Defaulting to PostgreSQL.")
        db_type = "postgresql"

    if db_type == "postgresql":
        repo = setup_postgresql_infrastructure()

        return Infrastructure(
            document_site_repository=repo,
            document_site_adapter=DocumentSiteAdapter(),
        )

    else:
        raise ValueError(
            f"Unsupported DB_TYPE: {db_type}. Supported types: postgresql."
        )
