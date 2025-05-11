from sqlmodel import create_engine
from sqlalchemy.engine import Engine

from src.environment import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT


def get_postgresql_url() -> str:
    """
    Generate a PostgreSQL connection URL.

    :return: A PostgreSQL connection URL.
    """

    host = DB_HOST
    database = DB_NAME
    user = DB_USER
    password = DB_PASSWORD
    port = DB_PORT or 5432

    if isinstance(port, str):
        port = int(port)

    if not host:
        raise ValueError("DB_HOST environment variable is not set.")
    if not database:
        raise ValueError("DB_NAME environment variable is not set.")
    if not user:
        raise ValueError("DB_USER environment variable is not set.")
    if not password:
        raise ValueError("DB_PASSWORD environment variable is not set.")

    return f"postgresql://{user}:{password}@{host}:{port}/{database}"


def create_postgresql_engine() -> Engine:
    """
    Create a PostgreSQL engine.

    :return: A SQLModel engine connected to the PostgreSQL database.
    """
    url = get_postgresql_url()
    return create_engine(url, echo=True)
