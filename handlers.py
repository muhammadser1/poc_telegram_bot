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


def generate_random_number(update: Update, context: CallbackContext) -> None:
    try:
        response = requests.post(f'{SERVER_URL}/random-numbers')
        if response.status_code == 200:
            data = response.json()
            update.message.reply_text(f"Server says: {data}")
        else:
            error_message = f"Server returned status code: {response.status_code}"
            if response.text:
                error_message += f"\nServer response: {response.text}"
            update.message.reply_text(error_message)


    except requests.RequestException as e:
        update.message.reply_text(f"Error fetching data: {e}")
