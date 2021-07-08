from aiogram.types import Message
from bot.config import dp
from bot.states import NewNoteStates
from bot.services.dbService.account_service import register_new_user, is_user_exist
from bot.services.dbService.note_service import get_notes_for_user


@dp.message_handler(commands="start", state="*")
async def hello_message_handler(message: Message):
    # TODO: ALTER THE MESSAGE TEXT
    if not is_user_exist(message.from_user.id):
        register_new_user(t_id=message.from_user.id)
        await message.answer("privet")
    else:
        await message.answer("welcome back")

    await NewNoteStates.waiting_for_note.set()


@dp.message_handler(commands="help", state="*")
async def help_message_handler(message: Message):
    # TODO: ALTER THE MESSAGE TEXT
    # IDEA: make help more specific (depend on current state).
    await message.answer("there is no help...")


@dp.message_handler(commands="list", state="*")
async def list_message_handler(message: Message):
    # TODO: ALTER THE MESSAGE TEXT
    # get list from db and print

    msg = "list of your spendings for the last month...\n\n"
    template = "{id} {name} -- {val}\n"
    for note in get_notes_for_user(t_id=message.from_user.id):
        msg += template.format(id=note.id, name=note.name, val=note.value)
    await message.answer(msg)

# TODO: MAKE A /menu COMMAND WITH EVERY FUNCTION AS CALLBACK QUERY BUTTONS
