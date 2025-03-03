from mongoengine import Document, StringField


class Admin(Document):
    username = StringField(required=True, min_length=1, max_length=50)
    name = StringField(required=True, min_length=1, max_length=50)
    surname = StringField(required=True, min_length=1, max_length=50)
