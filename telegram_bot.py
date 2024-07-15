import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

from handlers import *

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found. Please set it in the .env file.")


def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("test", test_command))
    dispatcher.add_handler(CommandHandler("test_server", test_server))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
