from ..share.connection import get_engine
from ..site.repository import SitePostgreSQLRepository


def setup_postgresql_infrastructure():
    """
    Setup PostgreSQL repository.
    """
    # Create the database engine
    engine = get_engine()

    # Create the repository
    return SitePostgreSQLRepository(engine)
