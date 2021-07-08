from peewee import IntegerField, CharField, DateTimeField, TextField
from datetime import datetime

from .base import BaseModel


class NoteModel(BaseModel):
    name = CharField(max_length=128)

    value = IntegerField()

    currency = CharField(max_length=3, null=True)

    description = TextField(null=True)

    created_at = DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'NoteModel'
