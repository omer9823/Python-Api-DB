from .base import Base
from .engine import engine
from app.models import user  # noqa: F401  ← ייבוא כל המודלים

def init_db() -> None:
    Base.metadata.create_all(bind=engine)