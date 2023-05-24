# import os
# import csv
# from dotenv import load_dotenv
#
# load_dotenv('.env')
# TOKEN = os.getenv('TOKEN')
#
# import logging
# import os
#
# from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestChat, KeyboardButtonRequestUser, \
    KeyboardButtonPollType, WebAppInfo
# from dotenv import load_dotenv
#
# load_dotenv('.env')
#
# API_TOKEN = os.getenv('TOKEN')
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(API_TOKEN)
# dp = Dispatcher(bot)
#
# regions = list(csv.reader(open('regions.csv')))
#
#
# # button
# #
# @dp.message_handler(commands=['start', 'help'])
# async def welcome(message: types.Message):
#     rkm = ReplyKeyboardMarkup(resize_keyboard=True)
#
#     await message.answer('Viloyatlar', reply_markup=rkm)
#
#
# @dp.message_handler(lambda msg: msg.text == 'Orqaga')
# async def back(message: types.Message):
#     await welcome(message)
#
#
# @dp.message_handler(lambda msg: msg.text in (''))
# async def districkts(message: types.Message):
#     rkm = ReplyKeyboardMarkup(resize_keyboard=True)
#     if message.text == 'Toshkent':
#         rkm.add('Yunusobod')
#         rkm.add('Chilonzor')
#     else:
#         rkm.add('Urgut')
#         rkm.add('JOnboy')
#     rkm.add('Orqaga')
#     await message.answer(f'{message.text} tumanlari', reply_markup=rkm)
#
#
# # rkm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
# #     # rkm.row('btn 1', 'btn 2', 'btn 3', 'btn 4')
# #     # rkm.add('btn 1', 'btn 2', 'btn 3', 'btn 4')
# #     # req_chat = KeyboardButtonRequestChat(1, False)
# #     # req_user = KeyboardButtonRequestUser(1)
# #     # poll_type = KeyboardButtonPollType()
# #     # web_app_info = WebAppInfo(url='https://core.telegram.org/bots/api#chatshared')
# #     rkm.add(
# #         KeyboardButton('location', request_location=True),
# #         KeyboardButton('number', request_contact=True),
# #         # KeyboardButton('chat', request_chat=req_chat),
# #         # KeyboardButton('user', request_user=req_user),
# #         # KeyboardButton('poll', request_poll=poll_type),
# #         # KeyboardButton('webapp', web_app=web_app_info)
# #     )
# #     print(message.from_user.id, message.from_user.first_name, message.from_user.username)
# #     await message.answer('Xush kelibsiz!', reply_markup=rkm)
# #
# #
# # @dp.message_handler(content_types=types.ContentTypes.CHAT_SHARED)
# # async def echo(message: types.Message):
# #     await message.answer(message.text)
# #
# #
# # @dp.message_handler(content_types=types.ContentTypes.USER_SHARED)
# # async def echo(message: types.Message):
# #     await message.answer(message.text)
# #
# #
# # @dp.message_handler(content_types=types.ContentTypes.CONTACT)
# # async def echo(message: types.Message):
# #     text = ' '.join([str(message.contact.phone_number), message.from_user.first_name, str(message.from_user.id)])
# #     print(text)
# #     # await bot.send_message(514411336, text)
# #     await message.answer(text)
# #
# #
# # @dp.message_handler(content_types=types.ContentTypes.LOCATION)
# # async def echo(message: types.Message):
# #     text = str(message.location.latitude) + ' ---- ' + str(message.location.longitude)
# #     await message.answer(text)
# #
# #
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
import csv
import logging
import os

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, ParseMode
from dotenv import load_dotenv

register_time = State()
logging.basicConfig(level=logging.INFO)

load_dotenv('.env')

API_TOKEN = os.getenv('TOKEN')
bot = Bot(API_TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

'''

ism,
familya,
tel, 935001010
qaysi gruppa(beginner, elementary, intermediate, upper-intermediate, ielts),
vaqti

'''


class Form(StatesGroup):
    Ism = State()
    Yosh = State()
    Viloyatlar = State()
    Tumani = State()


def get_regions():
    with open('regions.csv') as f:
        regions = {str(row): 0 for row in csv.reader(f)}

        return dict(regions)


def get_districts():
    with open('districts.csv') as f:
        districts = {}
        for row in csv.reader(f):
            if len(row) == 3:
                districts[row[1]] = row[2]

        return districts


regions = get_regions()

districts = get_districts()


@dp.message_handler(commands=['start'])
async def start_menu(message: Message):
    await Form.Ism.set()
    await message.answer('Xush kelibsiz\n ismingizni kiriting!')


@dp.message_handler(state=Form.Ism)
async def get_username(message: Message, state: FSMContext):
    await state.update_data(Ism=message.text)
    await Form.next()
    await message.answer('Yoshingizni kiriting')

@dp.message_handler(state=Form.Yosh)
async def get_username(message: Message, state: FSMContext):
    await state.update_data(Yosh=message.text)
    await Form.next()
    await message.answer('Viloyatlarni kiriting')


@dp.message_handler(lambda msg: msg.text in regions.keys(), state=Form.Viloyatlar)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(Viloyarlar=message.text)
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    rkm.add(*regions.keys())
    await message.answer('Viloyatlar', reply_markup=rkm)


@dp.message_handler(lambda msg: msg.text.title() not in regions, state=Form.Viloyatlar)
async def get_phone(message: Message):
    text = 'Viloyatni togri kiriting\n' + ' '.join(regions.keys())

    await message.answer(text)


@dp.message_handler(state=Form.Tumani)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(Tumani=message.text)
    await Form.next()
    text = 'tumanni tanlang\n' + ' '.join(districts)
    await message.answer(text)


@dp.message_handler(lambda msg: msg.text.title() not in districts, state=Form.Viloyatlar)
async def get_phone(message: Message):
    text = 'tumanni togri kiriting\n' + ' '.join(districts)
    await message.answer(text)


# Dushanba
# Toq kunlari
# ertalabka
# 14:00

@dp.message_handler(state=Form.states)
async def get_username(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['Viloyatlar'] = message.text

        text = md.text(
            md.text(md.code('Sizning malumotlaringiz')),
            md.text(md.bold('Ism:'), data['Ism']),
            md.text(md.bold('Yosh:'), data['Yosh']),
            md.text(md.bold('Viloyatlar:'), data['Viloyatlar']),
            md.text(md.bold('tumani:'), data['tumani']),
            sep='\n'
        )
        await message.answer(text, parse_mode=ParseMode.MARKDOWN)

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

#
#
# def get_regions():
#     with open('regions.csv') as f:
#         regions = {name: _id for _id, name in csv.reader(f)}
#         return dict(regions)
#
#
# def get_districts():
#     with open('districts.csv') as f:
#         districts = {name: region for _, name, region in csv.reader(f)}
#         return districts
#
#
# regions = get_regions()
# districts = get_districts()


# @dp.message_handler(commands=['start', 'help'])
# async def welcome(message: types.Message):
#     rkm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
#     rkm.add(*regions.keys())
#     await message.answer('Viloyatlar', reply_markup=rkm)


#
# @dp.message_handler(lambda msg: msg.text == BUTTONS['back'])
# async def back_mene(message: types.Message):
#     await welcome(message)


# @dp.message_handler(lambda msg: msg.text in regions.keys())
# async def get_districts(message: types.Message):
#     region_id = regions.get(message.text)
#     d = [name for name, r_id in districts.items() if r_id == region_id]
#
#     rkm = ReplyKeyboardMarkup(resize_keyboard=True)
#     rkm.add(*d)
#     rkm.add(BUTTONS['back'])
#     await message.answer(f'{message.text} tumanlari', reply_markup=rkm)
#
#
# @dp.message_handler()
# async def get_districts(message: types.Message):
#     rkm = ReplyKeyboardRemove()
#     text = 'Xato malumot kiritildi /start bosing'
#     await message.answer(text, reply_markup=rkm)


'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''------------------------------------------------
'''
#
#
# def get_regions():
#     with open('regions.csv') as f:
#         regions = {name: _id for _id, name in csv.reader(f)}
#         return dict(regions)
#
#
# def get_districts():
#     with open('districts.csv') as f:
#         districts = {name: region for _, name, region in csv.reader(f)}
#         return districts
#
#
# regions = get_regions()
# districts = get_districts()
#
#
# @dp.message_handler(lambda msg: msg.text in regions.keys())
# async def get_districts(message: types.Message):
#     region_id = regions.get(message.text)
#     d = [name for name, r_id in districts.items() if r_id == region_id]
#
#     rkm = ReplyKeyboardMarkup(resize_keyboard=True)
#     rkm.add(*d)
#     await message.answer(f'{message.text} tumanlari', reply_markup=rkm)
#
#
# @dp.message_handler(commands=['start'])
# async def welcome(message: types.Message):
#     ikm = InlineKeyboardMarkup()
#     ikm.add(InlineKeyboardButton('btn1', callback_data='1'))
#     ikm.add(InlineKeyboardButton('btn2', callback_data='2'))
#     await message.answer('inline buttons', reply_markup=ikm)
#
#
# @dp.message_handler()
# async def welcome(callback: types.CallbackQuery):
#     await callback.message.answer(callback.data)
#     await callback.answer(f'javob{callback.data}')
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
import logging
from aiogram import Bot, Dispatcher, types

# Botning tokenini yozing
TOKEN = '6042323895:AAGkh0e43xid2Oyqoysoq-rrVJu5GOkDfB4'

# Bot obyekti yaratamiz
bot = Bot(token=TOKEN)

async def get_chat_id():
    try:
        # Botning chat_id ni olish uchun /start buyrug'i jo'natamiz
        await bot.send_message(chat_id='@your_chat_username', text='/start')
    except Exception as e:
        logging.exception(e)

async def on_message(message: types.Message):
    # Chat_id ni olish
    chat_id = message.chat.id
    print(f"Chat ID: {chat_id}")

if __name__ == '__main__':
    # Botni ishga tushiramiz
    from aiogram import executor
    from aiogram.types import ParseMode

    logging.basicConfig(level=logging.INFO)

    # Dispatcher obyekti
    dp = Dispatcher(bot)

    # Xabar kelganda on_message funksiyasini ishlatamiz
    dp.register_message_handler(on_message)

    executor.start_polling(dp, skip_updates=True)
