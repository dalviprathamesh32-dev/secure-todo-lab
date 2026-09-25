from sqlalchemy.orm import DeclarativeBase , sessionmaker
from sqlalchemy import create_engine
from core.config import settings

connect_args = (
    {"check_same_thread": False} if settings.DB_URL.startswith("sqlite") else {}
)

engine = create_engine(
    settings.DB_URL,
    echo=True
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

class Base(DeclarativeBase):
    pass


def get_db():
    db = Session()
    try :
        yield db
    finally :
        db.close()



