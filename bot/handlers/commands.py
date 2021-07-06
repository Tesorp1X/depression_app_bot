from aiogram.types import Message
from bot.run_server import dp
from bot.states import NewNoteStates


@dp.message_handler(commands="/start")
async def hello_message_handler(message: Message):
    # TODO: ALTER THE MESSAGE TEXT
    await message.answer("privet")
    await NewNoteStates.waiting_for_note.set()


@dp.message_handler(commands="/help")
async def help_message_handler(message: Message):
    # TODO: ALTER THE MESSAGE TEXT
    # IDEA: make help more specific (depend on current state).
    await message.answer("there is no help...")
