from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader

from db.connect import get_db
from src.libs.oath2 import get_current_user
from src.models import User
from src.repository.users import UsersRepository
from src.schemas.users import UserResponse, UserModel
from src.service_config import app_config

router = APIRouter(prefix="/users", tags=["users"])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse, name='SignUp User',
             description='SignUp User')
async def create_user(user: UserModel, db: Session = Depends(get_db)):
    user: User = await UsersRepository.create_user(user, db)
    return user


@router.patch('/avatar', response_model=UserResponse)
async def update_avatar_user(file: UploadFile = File(), current_user: User = Depends(get_current_user),
                             db: Session = Depends(get_db)):
    config = cloudinary.config(
        cloud_name=app_config['cloudinary']['cloud_name'],
        api_key=app_config['cloudinary']['api_key'],
        api_secret=app_config['cloudinary']['api_secret'],
        secure=True
    )

    cloudinary.uploader.upload(file.file, public_id=f'NotesApp/{current_user.username}', unique_filename=False,
                               overwrite=True)
    srcURL = cloudinary.CloudinaryImage(f'NotesApp/{current_user.username}').build_url(width=250, height=250,
                                                                                       crop='fill')
    user = await UsersRepository.update_avatar(current_user.id, srcURL, db)
    return user
