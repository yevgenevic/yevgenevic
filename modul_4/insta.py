# import instaloader
#
# # Create an instance of the Instaloader class
# L = instaloader.Instaloader()
#
# # Retrieve a profile by its username
# profile = instaloader.Profile.from_username(L.context, 'yevgenevic')
#
# print("Username:", profile.username)
# print("Full name:", profile.full_name)
# print("Followers:", profile.followers)
# print("Following:", profile.followees)
# print("Number of posts:", profile.mediacount)
# print("Profile picture URL:", profile.profile_pic_url)
# print("Biography:", profile.biography)
# print("External URL:", profile.external_url)
# print("Is business account:", profile.is_business_account)
# print("Is private account:", profile.is_private)
# print("Is verified account:", profile.is_verified)
# print("Number of IGTV videos:", profile.igtvcount)
# follower = profile.get_followers()
# for i in follower:
#     print(i)




import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import instaloader

# Initializing the bot
bot = Bot(token='5953038101:AAFTin64k4wMJII6mqjLE7Eg_LsuD9uLGoE')
dp = Dispatcher(bot)

# Initializing the Instaloader
L = instaloader.Instaloader()

# Handler for the command /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! Send me an Instagram username to get the recent photos.")

# Handler for Instagram username
@dp.message_handler(func=lambda message: True)
async def handle_instagram_username(message: types.Message):
    try:
        username = message.text
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()
        for post in posts:
            await bot.send_photo(message.chat.id, photo=post.url, caption=post.caption)
    except Exception as e:
        await message.reply("Error occurred while processing the request")

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
