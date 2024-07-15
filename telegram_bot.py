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
    try:
        updater = Updater(BOT_TOKEN)
    except Exception as e:
        print(f"Failed to initialize the updater: {e}")
        return
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("test", test_command))
    dispatcher.add_handler(CommandHandler("test_server", test_server))
    dispatcher.add_handler(CommandHandler("generate_random_number", generate_random_number))
    dispatcher.add_handler(CommandHandler("pokemon", getPokemon))

    try:
        updater.start_polling()
    except Exception as e:
        print(f"Failed to start polling: {e}")
        return
    updater.idle()


if __name__ == '__main__':
    main()
