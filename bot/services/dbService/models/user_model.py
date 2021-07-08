from peewee import IntegerField, CharField, DateField
from datetime import datetime

from .base import BaseModel


class UserModel(BaseModel):
    t_id = IntegerField()

    alias = CharField(max_length=64, null=True)

    preferred_currency = CharField(max_length=3, null=True)

    joined_at = DateField(default=datetime.now)

    class Meta:
        db_table = 'UserModel'
