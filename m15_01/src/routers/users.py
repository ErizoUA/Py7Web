from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.connect import get_db
from src.libs.oath2 import create_access_token
from src.models import User
from src.repository.users import UsersRepository
from src.schemas.auth import Token
from src.libs.hash import Hash
from src.schemas.users import UserResponse, UserModel

router = APIRouter(prefix="/users", tags=["users"])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: UserModel, db: Session = Depends(get_db)):
    user: User = await UsersRepository.create_user(user, db)
    return user


@router.patch('/avatar', response_model=UserResponse)
async def update_avatar_user(user: UserModel, db: Session = Depends(get_db)):
    pass
