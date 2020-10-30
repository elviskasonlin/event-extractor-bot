"""
main.py

Currently Echoes incoming messages

To-do
- Going to need callbacks
- Going to need async await on (scene ID, reply, user ID) and handle things from there
"""

# SECTION: Import modules

import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from decouple import config

# ---
# SECTION: Get environment variables
# ---

API_TOKEN = ""
try:
   API_TOKEN = config('api_token')
except Exception as err:
    raise err
    print("Please insert the telegram bot api token")

DEBUG = config('debug', default=FALSE, cast=bool)

WEBHOOK_URL = "https://api.telegram.org/bot{}/".format{API_TOKEN}


# ---
# SECTION: Initialisation
# ---

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
# Note: Dispatcher handles and processes incoming updates
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ---
# SECTION: Bot logic
# ---

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.chat.id, message.text)

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    logging.warning("Shutting down...")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

