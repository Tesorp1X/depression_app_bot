from peewee import InternalError

from .models.base import db
from bot.services.dbService.models.note_model import NoteModel
from .models.user_model import UserModel


def create_tables():
    try:
        db.connect()
        db.create_tables([NoteModel, UserModel, ])
    except InternalError as px:
        print(str(px))
