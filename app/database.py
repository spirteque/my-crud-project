from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = 'postgresql://admin:admin@localhost:5433/my-crud-db'
engine = create_engine(DATABASE_URL, echo=True)


def init_db() -> None:
	SQLModel.metadata.create_all(engine)


def get_session() -> Session:
	return Session(engine)
