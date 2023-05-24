import logging

import requests
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5845682729:AAHv4yltpFmH0lzP48cVTPZMLFMf0sBzmg8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_menu(message: types.Message):
    await bot.send_message(message.chat.id, 'Assalomu aleykum')


@dp.message_handler(commands=['start'])
async def start_menu(message: types.Message):
    url = 'https://ru.wikipedia.org/w/index.php?go=%search='
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    links = soup.find_all("div", class_="mw-search-heading")
    if len(links) > 0:
        url = 'https://ru.wikipedia.org' + links[0].find("a")["href"]





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

'''
pagination

https://limits.tginfo.me/en

'''
