from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from db.connect import get_db
from src.models import User
from src.service_config import app_config
from src.repository.users import UsersRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(app_config["auth"]["expire_token"]))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, app_config["auth"]["secret_key"], algorithm=app_config["auth"]["algorithm"])
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, app_config["auth"]["secret_key"], algorithms=[app_config["auth"]["algorithm"]])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user: User = await UsersRepository.get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user
