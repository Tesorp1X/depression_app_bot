import logging
import os
import re
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
