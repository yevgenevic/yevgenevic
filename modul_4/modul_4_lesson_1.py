# matrix = [
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4]
# ]
# for i in list(zip(*reversed(matrix))):
#     print(i)
#
# nums = [1, 2, 3, 1, 2, 3],
# k = 3
# seen = set()
# for i in range(len(nums)):
#     if tuple(nums[i]) in seen:
#         print(True)
#     seen.add(tuple(nums[i]))
#     if len(seen) > k:
#         seen.remove(tuple(nums[i - k]))
# print(False)


# k = 2
# n = 596785
#
# n = str(n)
# result = n[0]
# for i, v in enumerate(n[1:], 1):
#     if n[i - 1] >= n[i]:
#         k -= 1
#         if not k:
#             result = result[:-1] + n[i:]
#             break
#     result += v
# else:
#     result = result[:-1]
#
# print(result)

# matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
# min_ = [min(row) for row in matrix]
# max_ = [max(col) for col in zip(*matrix)]
# result = []
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] == min_[i] and matrix[i][j] == max_[j]:
#             result.append(matrix[i][j])
#
# print(result)

# s = '359'
# print(s.zfill(5))

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import asyncpg

# Replace <TOKEN> with your Telegram bot token
bot = Bot(token="6022432537:AAHV3uzklZfhqSUaGMW1_VN_mLE3iryRHpc")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# Replace <DATABASE_URL> with your PostgreSQL database URL
async def create_pool():
    pool = await asyncpg.create_pool(
        host="your_host",
        database="your_database",
        user="your_username",
        password="your_password"
    )
    return pool

loop = asyncio.get_event_loop()
pool = loop.run_until_complete(create_pool())

class PizzaOrder(StatesGroup):
    size = State()
    toppings = State()
    address = State()

# Start the order process with the /order command
@dp.message_handler(Command("order"))
async def cmd_order(message: types.Message):
    await message.answer("What size of pizza do you want? (Small/Medium/Large)")

    # Set the current state to 'size'
    await PizzaOrder.size.set()

# Handle the size of the pizza using an inline keyboard
@dp.message_handler(state=PizzaOrder.size)
async def process_size(message: types.Message, state: FSMContext):
    # Define the inline keyboard with buttons for each size option
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(
        InlineKeyboardButton("Small", callback_data="size_small"),
        InlineKeyboardButton("Medium", callback_data="size_medium"),
        InlineKeyboardButton("Large", callback_data="size_large"),
    )

    # Send the message with the inline keyboard
    await bot.send_message(message.chat.id, "Choose a size:", reply_markup=markup)

    # Save the selected size in the state
    await state.update_data(size=message.text)

    # Move to the next state 'toppings'
    await PizzaOrder.toppings.set()

# Handle the toppings of the pizza using an inline keyboard
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("topping_"), state=PizzaOrder.toppings)
async def process_toppings(callback_query: types.CallbackQuery, state: FSMContext):
    # Get the toppings from the callback data
    toppings = callback_query.data.split("_")[1:]

    # Define the inline keyboard with buttons for each topping option
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(
        InlineKeyboardButton("Pepperoni", callback_data="topping_pepperoni"),
        InlineKeyboardButton("Mushrooms", callback_data="topping_mushrooms"),
        InlineKeyboardButton("Onions", callback_data="topping_onions"),
        InlineKeyboardButton("Sausage", callback_data="topping_sausage"),
        InlineKeyboardButton("Bacon", callback_data="topping_bacon"),
    )

    # Send the message with the inline keyboard
    await bot.send_message(callback_query.from_user.id, "Choose toppings:", reply_markup=markup)

    # Save the selected toppings in the state
    await state.update_data(toppings=toppings)

    # Move to the next state 'address'
    await PizzaOrder.address.set()

# Handle the address of the pizza using a regular text message
@dp.message_handler(state=PizzaOrder.address)
async def process_address(message: types.Message, state: FSMContext):
    # Save the address in the state
    await state.update_data(address=message.text)

    # Get the data from the
    data = await state.get_data()

    # Get the size, toppings, and address from the state data
    size = data.get("size")
    toppings = data.get("toppings")
    address = data.get("address")

    # Create the order summary message
    order_summary = f"Order summary:\n\nSize: {size}\nToppings: {', '.join(toppings)}\nAddress: {address}"

    # Save the order in the database
    async with pool.acquire() as conn:
        await conn.execute("INSERT INTO pizza_orders (size, toppings, address) VALUES ($1, $2, $3)", size, toppings,
                           address)

    # Send the order summary to the user
    await message.answer(order_summary)

    # End the conversation and reset the state
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
