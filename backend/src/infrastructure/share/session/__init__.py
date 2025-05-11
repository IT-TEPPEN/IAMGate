from .postgresql import get_postgresql_session
from src.environment import DB_TYPE


__all__ = [
    "get_session",
]


def get_session(engine):
    """
    Get a database session.

    :return: database session.
    """

    db_type = DB_TYPE

    if db_type is None:
        db_type = "postgresql"

    if db_type == "postgresql":
        return get_postgresql_session(engine)
    else:
        raise ValueError(
            f"Unsupported DB_TYPE: {db_type}. Supported types: postgresql."
        )
