import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6042323895:AAGkh0e43xid2Oyqoysoq-rrVJu5GOkDfB4'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def hello(message: types.Message):
    try:
        await message.answer('assalomu aleykum nma xizmat')
        await message.delete()
    except:
        await message.reply('birinchi menga azo bulin')


@dp.message_handler(commands=['open'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'ertalab 8 dan kechga 8 gacha')


@dp.message_handler(commands=['location'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'manzil chorsuda')


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)
    if message.text == 'salom':
        await message.answer('sziga ham salom')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
