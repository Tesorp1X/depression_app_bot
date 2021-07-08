from aiogram import Dispatcher

from bot.config import dp, executor, displayed_commands, bot
from bot.services.dbService.helper import create_tables
from bot.handlers import commands, messages, callbacks


async def on_startup(dispatcher: Dispatcher):
    """
        Creates tables if they don't exist and sets displayed commands.
    """
    create_tables()
    await bot.set_my_commands(commands=displayed_commands)


if __name__ == '__main__':
    executor.on_startup(on_startup)
    executor.start_polling(dp)
