import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

BOT_TOKEN = os.getenv('TOKEN', 'default_token_value')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_message(message: types.Message):
    unli = sum(c.isalpha() and c.lower() in 'aeiou' for c in message.text)

    if unli >= 5:
        await message.delete()
    else:
        await message.answer('unli harflar 5 tadan kam')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


