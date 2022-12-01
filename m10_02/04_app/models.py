from mongoengine import Document, StringField, BooleanField, connect

connect(db='web7', host='mongodb://localhost:27017')


class Contact(Document):
    email = StringField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    completed = BooleanField(default=False)
    meta = {'collection': 'contacts'}
