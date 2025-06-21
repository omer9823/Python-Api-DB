from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.db.repositories.user_repository import UserRepository

def create_user_service(db: Session, user_in: UserCreate):
    # ולידציה ייחודית/עסקית
    if UserRepository.get_user_by_email(db, user_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return UserRepository.create_user(db, user_in)