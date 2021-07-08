from sqlite3 import InternalError

from .models.user_model import UserModel


def is_user_exist(t_id: int) -> bool:
    if UserModel.get_or_none(t_id=t_id):
        return True
    return False


def register_new_user(t_id: int, alias: str = None, currency: str = None):
    try:
        UserModel.create(t_id=t_id,
                         alias=alias,
                         preferred_currency=currency)
    except InternalError as exc:
        # asyncio.run(utils.make_broadcast(f"Alert! Problem with database: {exc}", ADMINS_IDS))

        UserModel.create(t_id=t_id,
                         alias=alias,
                         preferred_currency=currency)

