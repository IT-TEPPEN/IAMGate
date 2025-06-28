from sqlmodel import Session


from src.environment import DB_TYPE


def get_postgresql_session(engine):
    """
    Get a database session.

    :return: A SQLModel session connected to the database.
    """
    return Session(engine)
