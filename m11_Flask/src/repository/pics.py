from sqlalchemy import and_

from src import models, db
from src.libs.file_service import move_user_picture, delete_user_picture


def get_pictures_user(user_id):
    return db.session.query(models.Picture).filter(models.Picture.user_id == user_id).all()


def get_picture_user(pic_id, user_id):
    return db.session.query(models.Picture).filter(
        and_(models.Picture.user_id == user_id, models.Picture.id == pic_id)).first()


def upload_file_for_user(user_id, file_path, description):
    new_filename, size = move_user_picture(user_id, file_path)
    picture = models.Picture(description=description, user_id=user_id, path=new_filename, size=size)
    db.session.add(picture)
    db.session.commit()


def update_picture(pic_id, user_id, description):
    pic = get_picture_user(pic_id, user_id)
    pic.description = description
    db.session.commit()


def delete_picture_user(pic_id, user_id):
    delete_user_picture(get_picture_user(pic_id, user_id).path)
    db.session.query(models.Picture).filter(
        and_(models.Picture.user_id == user_id, models.Picture.id == pic_id)).delete()
    db.session.commit()
