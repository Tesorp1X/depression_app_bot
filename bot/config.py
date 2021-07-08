import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import Executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Getting envs
API_TOKEN = os.getenv("API_TOKEN")
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT', 5432)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

storage = MemoryStorage()


displayed_commands = [
    types.BotCommand(command="/help", description="Список доступынх команд"),

]

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
executor = Executor(dp, skip_updates=True)
