from aiogram.types import Message, ParseMode
from aiogram.dispatcher import FSMContext

import re

from bot.config import dp
from bot.states import NewNoteStates, EditNoteStates
from bot.services.note_service import create_new_note, alter_note
from bot.handlers.commands import list_message_handler


@dp.message_handler(lambda mes: not mes.text.startswith("/"), state=NewNoteStates.waiting_for_note)
async def new_note_message_handler(message: Message, state: FSMContext):
    # parse
    text = message.text
    pattern = re.compile(r"\d+\s[\w\s\S_-]+")
    if re.fullmatch(pattern, text.lower()):
        value, name = re.split(r' ', message.text, maxsplit=1)
        # save data and ask for description
        new_note_id = create_new_note(name, value, message.from_user.id)
        # TODO: add error-check
        await state.update_data(last_added_note=new_note_id)

        await message.answer(f"note is saved. if u want to add description use /description{new_note_id}." +
                             "\n\ntype /list to see recent notes.")
    elif re.fullmatch(r"\d+\s*", text.lower()):
        value = int(text)
        await state.update_data(value=value)
        await message.answer("what did you spent that much money on?")
        await EditNoteStates.waiting_for_new_name.set()
    else:
        await message.answer("*ERROR: incorrect message.*\n\npattern looks like that: \"value name\".",
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


@dp.message_handler(state=NewNoteStates.waiting_for_description)
async def add_description_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    note_id = data['note_id']
    description_txt = message.text
    alter_note(note_id=note_id, description_txt=description_txt)

    if 'last_notes' in data.keys():
        last_notes = data.get('last_notes')
        for note in last_notes:
            if note.id == note_id:
                note.description = description_txt
                break

    await state.set_data(data)
    await NewNoteStates.waiting_for_note.set()
    await message.answer("note modified!")
    message.text = "/list"
    await list_message_handler(message, state)


@dp.message_handler(lambda mes: mes.text.startswith("/"), state="*")
async def garbage_collector_handler(message: Message, state: FSMContext):
    await message.answer("Unknown command. Use /help to find out how to use this bot.")
