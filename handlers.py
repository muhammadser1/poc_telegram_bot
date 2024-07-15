from telegram import Update
from telegram.ext import CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello ! This is your bot.')


def test_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('this is a response from the /test command.')


start_handler = CommandHandler("start", start)
test_command_handler = CommandHandler("test", test_command)
