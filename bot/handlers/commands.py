from aiogram.types import Message, ParseMode
from aiogram.dispatcher import FSMContext

from bot.config import dp
from bot.states import NewNoteStates
from bot.services.account_service import register_new_user, is_user_exist
from bot.services.note_service import get_notes_for_user, get_note_by_id


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
async def list_message_handler(message: Message, state: FSMContext):
    # TODO: ALTER THE MESSAGE TEXT
    # get list from db and print

    msg = "list of your spendings for the last month...\n\n"
    template = "{name} -- {val} /more{id} /del{id}\n"
    last_notes = get_notes_for_user(t_id=message.from_user.id)
    await state.update_data(last_notes=last_notes)
    for note in last_notes:
        msg += template.format(id=note.id, name=note.name, val=note.value)
    await message.answer(msg)

# TODO: MAKE A /menu COMMAND WITH EVERY FUNCTION AS CALLBACK QUERY BUTTONS


@dp.message_handler(lambda message: message.text.startswith('/more'))
async def more_message_handler(message: Message, state: FSMContext):
    note_id = int(message.text[5:])

    data = await state.get_data()
    is_note_found = False
    if 'last_notes' in data.keys():
        last_notes = data.get('last_notes')
        for note in last_notes:
            if note.id == note_id:
                that_note = note
                is_note_found = True

    if not is_note_found:
        # last_notes = get_notes_for_user(t_id=message.from_user.id)
        # data['last_notes'] = last_notes
        that_note = get_note_by_id(note_id)

    description = "*Note description:*" + that_note.description \
        if that_note.description else "*This note doesn't have a description.*"
    msg = f"*#{that_note.id} {that_note.name}@{that_note.created_at}*\n\n{description}"

    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(lambda message: message.text.startswith('/del'))
async def more_message_handler(message: Message, state: FSMContext):
    note_id = int(message.text[4:])

    await message.answer("this function doesn't implemented yet.")
