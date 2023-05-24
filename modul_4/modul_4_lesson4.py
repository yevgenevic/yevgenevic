# for post in profile.get_posts():
#     L.download_post(post, target=f"{profile.username}/{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}")
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

# import instaloader
#
# # Create an instance of the Instaloader class
# L = instaloader.Instaloader()
#
# # Retrieve a profile by its username
# profile = instaloader.Profile.from_username(L.context, 'username')
#
# # Create a folder for the videos
# folder_name = profile.username + "_videos"
# L.context.log("info", f"Creating folder {folder_name}")
# L.context.push_directory(folder_name)
#
# # Iterate through all the posts of the profile
# for post in profile.get_posts():
#     # Check if the post is a video
#     if post.is_video:
#         # Download the video and save it to a file
#         L.context.log("info", f"Downloading {post.owner_username}/{post.shortcode}")
#         L.download_video(post, post.date_utc.strftime('%Y-%m-%d_%H-%M-%S'))
#
# # Switch back to the parent directory
# L.context.pop_directory()


# import instaloader
#
# # Create an instance of the Instaloader class
# L = instaloader.Instaloader()
#
# # Retrieve a profile by its username
# profile = instaloader.Profile.from_username(L.context, 'username')
#
# # Print profile information
# print("Username:", profile.username)
# print("Full name:", profile.full_name)
# print("Followers:", profile.followers)
# print("Following:", profile.followees)
#
# # Download the profile picture
# L.download_profilepic(profile.username)
#
# # Download all the posts of the profile
# L.download_profile(profile.username, profile_pic=True, download_video_thumbnails=False)
#
# # Iterate through all the posts of the profile
# for post in profile.get_posts():
#     # Print the post caption and date
#     print("Caption:", post.caption)
#     print("Date:", post.date)
#
#     # Download the post
#     L.download_post(post, target=profile.username)
# import io
#
# import instaloader
# from aiogram import Bot, Dispatcher, executor
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
#
# # Create an instance of the Instaloader class
# L = instaloader.Instaloader()
#
# # Initialize the bot and dispatcher objects
# bot = Bot(token='5953038101:AAFTin64k4wMJII6mqjLE7Eg_LsuD9uLGoE')
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['insta'])
# async def handle_insta_command(message: Message):
#     # Check that the command has the correct format
#     command = message.text.split()
#     if len(command) != 2:
#         await message.reply("Usage: /insta <username>")
#         return
#
#     # Retrieve a profile by its username
#     profile = instaloader.Profile.from_username(L.context, command[1])
#
#     # Send the profile information to the user
#     await message.reply(
#         f"Username: {profile.username}\nFull name: {profile.full_name}\nFollowers: {profile.followers}\nFollowing: {profile.followees}")
#
#     # Retrieve the profile photo
#     bio = io.BytesIO()
#     L.download_profilepic(profile)
#     bio.seek(0)
#     try:
#     # Send the profile photo to the user
#         await message.reply_photo(photo=bio)
#     except Exception as e:
#         # handle all other exceptions here
#         print(f"An unknown exception occurred: {e}")
#
#     # Ask the user if they want to see the profile's posts
#     await message.reply("Do you want to see this user's posts?", reply_markup=ReplyKeyboardMarkup(
#         [[KeyboardButton("Yes"), KeyboardButton("No")]], resize_keyboard=True, one_time_keyboard=True))
#
#     # Wait for the user's response
#     async with dp.current_state(chat=message.chat.id, user=message.from_user.id) as state:
#         await state.set_state("WAITING_FOR_RESPONSE")
#
#     # Process the user's response
#     async with dp.current_state(chat=message.chat.id, user=message.from_user.id) as state:
#         if await state.get_state() == "WAITING_FOR_RESPONSE":
#             if message.text == "Yes":
#                 # Retrieve the profile's media
#                 for post in profile.get_posts():
#                     # Download the media file to a BytesIO object
#                     media = io.BytesIO()
#                     if post.is_video:
#                         L.download_video(post, media)
#                     else:
#                         L.download_post(post, media)
#                     media.seek(0)
#
#                     # Send the media file to the user
#                     if post.is_video:
#                         await message.reply_video(video=media)
#                     else:
#                         await message.reply_photo(photo=media)
#             else:
#                 await message.reply("Okay, no problem.")
#                 await state.reset_state()
#
#
# # Start the bot
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
'''
5953038101:AAFTin64k4wMJII6mqjLE7Eg_LsuD9uLGoE
lXzxQMX*wOsHRJPy
'''



import insta
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Initialize bot and dispatcher
bot = Bot(token="5953038101:AAFTin64k4wMJII6mqjLE7Eg_LsuD9uLGoE")
dp = Dispatcher(bot)

L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, 'yevgenevic')
markup = InlineKeyboardMarkup()
markup.row(
    InlineKeyboardButton("Profil rasmi", callback_data=f"photo_{profile.username}"),
    InlineKeyboardButton("Postlar", callback_data=f"posts_{profile.username}"),
    InlineKeyboardButton("Videolar", callback_data=f"videos_{profile.username}")
)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello, I'm your bot!", reply_markup=markup)


# Define inline query handler
@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    query = inline_query.query.strip()
    if not query:
        return
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, query)

    input_content = types.InputTextMessageContent(
        message_text=f"Ma'lumotlar: @{profile.username}"
    )
    result_id = str(hash(profile.username))
    await inline_query.answer(
        results=[types.InlineQueryResultArticle(
            id=result_id,
            title=f"@{profile.username}",
            input_message_content=input_content,
            reply_markup=markup
        )],
        cache_time=0
    )


# Define callback query handler for profile photo
@dp.callback_query_handler(lambda c: c.data.startswith('photo_'))
async def process_callback_profile_photo(callback_query: types.CallbackQuery):
    _, username = callback_query.data.split("_")
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    photo = profile.get_profile_pic()

    await bot.send_photo(
        callback_query.from_user.id,
        photo=photo,
        caption=f"@{username} profil rasmi"
    )


# Define callback query handler for profile posts
@dp.callback_query_handler(lambda c: c.data.startswith('posts_'))
async def process_callback_profile_posts(callback_query: types.CallbackQuery):
    _, username = callback_query.data.split("_")
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    posts = profile.get_posts()

    for post in posts:
        if not post.is_video:
            await bot.send_photo(
                callback_query.from_user.id,
                photo=post.url,
                caption=post.caption
            )


# Define callback query handler for profile videos
@dp.callback_query_handler(lambda c: c.data.startswith('videos_'))
async def process_callback_profile_video(callback_query: types.CallbackQuery):
    _, username = callback_query.data.split("_")
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    posts = profile.get_posts()

    for post in posts:
        if post.is_video:
            video_file = post.get_video_as_file()
            await bot.send_video(
                callback_query.from_user.id,
                video=video_file,
                caption=post.caption
            )


# Start the bot
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp)
