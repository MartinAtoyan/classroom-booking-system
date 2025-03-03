from mongoengine import Document, StringField, IntField, DateTimeField
from datetime import datetime


class ClassRoom(Document):
    name = StringField(required=True, min_length=1, max_length=50)
    capacity = IntField(required=True, min_value=1, max_value=100)
    feature = StringField(required=True, min_length=1, max_length=150)

    meta = {'allow_inheritance': True}

class BookRoom(ClassRoom):
    group_name = StringField(required=True, min_length=1, max_length=150)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    activity = StringField(required=True, min_length=1)

    def clean(self):
        if self.start_time and self.end_time:
            if self.start_time >= self.end_time:
                raise ValueError("start_time must be before end_time")

class CancelBooking(ClassRoom):
    group_name = StringField(required=True, min_length=1, max_length=150)
    cancel_time = DateTimeField(required=True, default=datetime.utcnow)
    description = StringField(required=True, min_length=1)
