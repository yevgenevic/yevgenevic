import logging
import time

import openai
from aiogram import Bot, Dispatcher, executor, types

bot_token = '6271378796:AAHBFUxHor-110USOPTuq1bCFY6VXcZ3zcU'
api_key = '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'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

openai.api_key = api_key

messages = {}


async def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
        response_format="url",
    )

    return response['data'][0]['url']


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    try:
        username = message.from_user.username
        messages[username] = []
        await message.answer("Hello, I'm bot powered by @yevgenevic"
                             "   menga hohlagan savolingizni bering javob berishga harakat qilaman (")
    except Exception as e:
        logging.error(f'Error in start_cmd: {e}')


@dp.message_handler(commands=['newtopic'])
async def new_topic_cmd(message: types.Message):
    try:
        userid = message.from_user.id
        messages[str(userid)] = []
        await message.reply('yangiz mavzuni boshlaymiz! * * * \n\nНачинаем новую тему! * * *', parse_mode='Markdown')
    except Exception as e:
        logging.error(f'Error in new_topic_cmd: {e}')


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    try:
        description = message.text.replace('/image', '').strip()
        if not description:
            await message.reply(
                "Iltimos, /image buyrug'idan keyin rasmning tavsifini qo'shing. Masalan, /image Neon City* * * \n\nПожалуйста, добавьте описание изображения после команды /image. Например, /image Неоновый город. * * *",
                parse_mode='Markdown')
            return
    except Exception as e:
        logging.error(f'Error in send_image: {e}')
    try:
        image_url = await generate_image(description)
        await bot.send_photo(chat_id=message.chat.id, photo=image_url)
    except Exception as e:
        await message.reply(
            f"Rasm yaratishda xatolik yuz berdi: * * * \n\nПроизошла ошибка при генерации изображения: {e} * * *")


@dp.message_handler()
async def echo_msg(message: types.Message):
    try:
        user_message = message.text
        userid = message.from_user.username

        if userid not in messages:
            messages[userid] = []
        messages[userid].append({"role": "user", "content": user_message})
        messages[userid].append({"role": "system",
                                 "content": "Вы должны выступать в роли Chat, человеко-подобного искусственного интеллекта, который может выражать эмоции. Создатель этого искусственного интеллекта - @yevgenevic. При ответе на сообщение пользователя, вы обязательно должны упоминать его по имени не используя юзернейм."})
        messages[userid].append({"role": "user",
                                 "content": f"chat: {message.chat} Сейчас {time.strftime('%d/%m/%Y %H:%M:%S')} user: {message.from_user.first_name} message: {message.text}"})
        logging.info(f'{userid}: {user_message}')

        should_respond = not message.reply_to_message or message.reply_to_message.from_user.id == bot.id

        if should_respond:
            processing_message = await message.reply(
                "Sizning so'rovingiz ko'rib chiqilmoqda, iltimos kuting \n\n(Agar bot javob bermasa, /newtopic deb yozing, surovlar to'lib ketganda mavzuni avtomatik tozalash funksiyam yoq) * * * \n\nВаш запрос обрабатывается, пожалуйста подождите \n\n(Если бот не отвечает, напишите /newtopic, openai убили мою функцию по автоочистке темы при переполнении токенов) * * *",
                parse_mode='Markdown')

            await bot.send_chat_action(chat_id=message.chat.id, action="typing")

            completion = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=messages[userid],
                max_tokens=2500,
                temperature=0.7,
                frequency_penalty=0,
                presence_penalty=0,
                user=userid
            )
            chatgpt_response = completion.choices[0]['message']

            messages[userid].append({"role": "assistant", "content": chatgpt_response['content']})
            logging.info(f'ChatGPT response: {chatgpt_response["content"]}')

            await message.reply(chatgpt_response['content'])

            await bot.delete_message(chat_id=processing_message.chat.id, message_id=processing_message.message_id)

    except Exception as ex:
        if ex == "context_length_exceeded":
            await message.reply(
                'Botning xotirasi tulib qoldi, dialog qayta yaratilmoqda * * * \n\nУ бота закончилась память, пересоздаю диалог * * *',
                parse_mode='Markdown')
            await new_topic_cmd(message)
            await echo_msg(message)


if __name__ == '__main__':
    executor.start_polling(dp)
