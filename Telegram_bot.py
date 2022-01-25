from telegram import *
from telegram.ext import *

bot = Bot("Use this token to access the HTTP API:")
# print(bot.get_me())
updater=Updater("Use this token to access the HTTP API:",use_context=True)

dispatcher=updater.dispatcher

def test_function(update:Update,context : CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Take Your starting Intro",
    )


start_value=CommandHandler('start',test_function)

dispatcher.add_handler(start_value)


def test_function(update:Update,context : CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, How are you",
    )


start_value=CommandHandler('hi',test_function)

dispatcher.add_handler(start_value)


def test_function1(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="How Can I Help You",
    )


start_value=CommandHandler('iamfine',test_function1)

dispatcher.add_handler(start_value)

# ==========================================My__Command=================================
print(bot.get_me())
updater.start_polling()
