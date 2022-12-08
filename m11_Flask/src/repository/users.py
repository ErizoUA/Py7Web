from src import db
from src import models
import bcrypt


def create_user(email, password, nick):
    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=10))
    user = models.User(username=nick, email=email, hash=hash)
    db.session.add(user)
    db.session.commit()
    return user

