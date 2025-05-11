from .postgresql import create_postgresql_engine

from src.environment import DB_TYPE

__all__ = [
    "get_engine",
]


def get_engine():
    db_type = DB_TYPE

    if db_type is None:
        print("DB_TYPE is not set. Defaulting to PostgreSQL.")
        db_type = "postgresql"

    if db_type == "postgresql":
        return create_postgresql_engine()
    else:
        raise ValueError(
            f"Unsupported DB_TYPE: {db_type}. Supported types: postgresql."
        )
