from peewee import IntegerField, CharField, DateTimeField, TextField, ForeignKeyField
from datetime import datetime

from bot.services.dbService.models.base import BaseModel
from bot.services.dbService.models.user_model import UserModel


class NoteModel(BaseModel):
    name = CharField(max_length=128)

    author = ForeignKeyField(UserModel)

    value = IntegerField()

    currency = CharField(max_length=3, null=True)

    description = TextField(null=True)

    created_at = DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'NoteModel'
