from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.connect import get_db
from src.libs.oath2 import create_access_token
from src.models import User
from src.repository.users import UsersRepository
from src.schemas.auth import Token
from src.libs.hash import Hash

router = APIRouter(prefix="/token", tags=["auth"])


@router.post("/", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user: User = await UsersRepository.get_user_by_email(db, form_data.username)
    if not user:
        raise credentials_exception
    if not Hash.verify_password(form_data.password, user.password):
        raise credentials_exception

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
