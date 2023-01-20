from sqlalchemy.orm import Session
from libgravatar import Gravatar

from src.libs.hash import Hash
from src.models import User
from src.schemas.users import UserModel


class UsersRepository:

    @staticmethod
    async def get_user_by_email(db: Session, email: str) -> User:
        user = db.query(User).filter(User.email == email).first()
        return user

    @staticmethod
    async def create_user(user: UserModel, db: Session) -> User:
        avatar = None
        try:
            g = Gravatar(user.email)
            avatar = g.get_image()
        except Exception as e:
            print(e)

        new_user = User(username=user.username, email=user.email, password=Hash.get_password_hash(user.password),
                        avatar=avatar)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    async def update_avatar(id_, url: str, db: Session):
        user = db.query(User).filter(User.id == id_).first()
        if user:
            user.avatar = url
        return user
