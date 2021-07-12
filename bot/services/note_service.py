from sqlite3 import InternalError

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


def get_notes_for_user(t_id: int, amount=3) -> Optional[List[NoteModel]]:
    # TODO: check date
    query = (NoteModel.select().join(UserModel).where(UserModel.t_id == t_id))

    return [note for note in query]


def get_note_by_id(note_id: int) -> Optional[NoteModel]:
    return NoteModel.get_or_none(id=note_id)


def delete_note_by_id(note_id: int) -> bool:
    note = NoteModel.get_or_none(id=note_id)

    if note:
        # NoteModel.delete_by_id(note_id)
        note.delete_instance()
        return True

    return False
