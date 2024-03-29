from sqlite3 import InternalError
from datetime import date, datetime

from typing import Optional, List

from bot.services.dbService.models.note_model import NoteModel
from bot.services.dbService.models.user_model import UserModel


def create_new_note(name: str, value: int, author_t_id: int,
                    currency: str = None, description: str = None):
    author = UserModel.get_or_none(t_id=author_t_id)

    if author is None:
        return -1

    try:
        note = NoteModel.create(name=name,
                                value=value,
                                author=author,
                                currency=currency,
                                description=description)
    except InternalError as exc:
        # asyncio.run(utils.make_broadcast(f"Alert! Problem with database: {exc}", ADMINS_IDS))
        note = NoteModel.create(name=name,
                                value=value,
                                author=author,
                                currency=currency,
                                description=description)

    return note.get_id()


def alter_note(note_id: int, new_name: str = None, new_value: int = None, description_txt: str = None):
    note = NoteModel.get_or_none(id=note_id)

    if note:
        if description_txt:
            note.description = description_txt
        if new_name:
            note.name = new_name
        if new_value:
            note.value = new_value

        try:
            note.save()
        except InternalError as exc:
            # asyncio.run(utils.make_broadcast(f"Alert! Problem with database: {exc}", ADMINS_IDS))

            note.save()


def get_notes_for_user(t_id: int,
                       since_that_date: datetime = datetime.combine(date.today(), datetime.min.time())) \
        -> Optional[List[NoteModel]]:
    predicate = (UserModel.t_id == t_id) & (NoteModel.created_at > since_that_date)
    query = (NoteModel.select().join(UserModel).where(predicate))

    return [note for note in query]


def get_note_by_id(note_id: int) -> Optional[NoteModel]:
    return NoteModel.get_or_none(id=note_id)


def delete_note_by_id(note_id: int) -> bool:
    note = NoteModel.get_or_none(id=note_id)

    if note:
        # NoteModel.delete_by_id(note_id)
        try:
            note.delete_instance()
            return True
        except InternalError as exc:
            # TODO: notify admin.
            print(exc)
            return False

    return False
