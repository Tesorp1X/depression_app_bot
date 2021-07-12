from aiogram.types import Message, ParseMode
from aiogram.dispatcher import FSMContext

import re

from bot.config import dp
from bot.states import NewNoteStates, EditNoteStates
from bot.services.note_service import create_new_note


@dp.message_handler(state=NewNoteStates.waiting_for_note)
async def new_note_message_handler(message: Message, state: FSMContext):
    # parse
    text = message.text
    pattern = re.compile(r"\d+\s[\w\s_-]+")
    if re.fullmatch(pattern, text.lower()):
        value, name = re.split(r' ', message.text, maxsplit=1)
        # save data and ask for description
        create_new_note(name, value, message.from_user.id)
        await message.answer("note is saved.")
    elif re.fullmatch(r"\d+\s*", text.lower()):
        value = int(text)
        await state.update_data(value=value)
        await message.answer("what did you spent that much money on?")
        await EditNoteStates.waiting_for_new_name.set()
    else:
        await message.answer("*ERROR: incorrect message.*\n\n pattern looks like that: \"value name\".",
                             parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(state=EditNoteStates.waiting_for_new_name)
async def new_note_name_message_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    name = message.text
    value = data.get("value")
    # save data and clear the context
    create_new_note(name, value, message.from_user.id)
    data.pop("value")
    await message.answer("note is saved.")
    await state.set_data(data)
    await NewNoteStates.waiting_for_note.set()
