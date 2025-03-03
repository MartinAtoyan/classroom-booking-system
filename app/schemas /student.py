import re
from mongoengine import Document, StringField, DateTimeField, EnumField
from datetime import datetime
from enum import Enum

class Role(Enum):
    admin = "Admin"
    student = "Student"

def validate_phone_number(phone):
    if not re.match(r"^\+?\d{9,15}$", phone):
        raise ValueError("Invalid phone number format. Example: +37411222333")

class User(Document):
    name = StringField(required=True, min_length=1, max_length=50)
    surname = StringField(required=True, min_length=1, max_length=50)
    group_name = StringField(required=True, min_length=1, max_length=50)
    phone_number = StringField(required=True, min_length=6, max_length=20, validation=validate_phone_number)
    role = EnumField(Role, required=True)

    meta = {'allow_inheritance': True}

class CreateUser(User):
    created_at = DateTimeField(default=datetime.now, required=True)

class DeleteUser(User):
    description = StringField(required=True, min_length=1)
