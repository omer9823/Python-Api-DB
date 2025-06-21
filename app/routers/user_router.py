from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_dto import UserCreate
from app.services.users import create_user_service
from app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(
    user_in: UserCreate,
    db: Session = Depends(get_db),
):
    return create_user_service(db, user_in)