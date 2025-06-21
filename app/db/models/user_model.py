from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) # on future versions it will be UUID
    name = Column(String, nullable=False)
    email = Column(String(320), unique=True, index=True, nullable=False)
    #hashed_password = Column(String(128), nullable=False)
    #is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())