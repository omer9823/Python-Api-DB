from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    def create_user(db: Session, user_in: UserCreate) -> User:
        db_user = User(**user_in.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user