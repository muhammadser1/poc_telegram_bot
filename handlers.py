from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import requests

from constants import SERVER_URL


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello ! This is your bot.')


def test_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('this is a response from the /test command.')


def test_server(update: Update, context: CallbackContext) -> None:
    try:
        response = requests.get(f'{SERVER_URL}/')
        data = response.json()
        update.message.reply_text(f"Server says: {data}")
    except requests.RequestException as e:
        update.message.reply_text(f"Error fetching data: {e}")


# start_server = CommandHandler("test_server", test_server)
# start_handler = CommandHandler("start", start)
# test_command_handler = CommandHandler("test", test_command)
