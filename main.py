import telegram.ext
from telegram.ext import updater

import Constents as keys
import Responses as R

print("Bot Started.....")

def start_command(update, context):
    update.message.reply_text("Hi dear,\nWelcome to Sanila Ranatunga's Official Assistant bot🤗🔥/help")

def help_command(update, context):
    update.message.reply_text("I can help you to connect with Sanila within seconds\n\n"
                              "1 - Who am I\n"
                              "2 - To connect with Sanila Ranatunga\n"
                              "3 - Report bugs\n"
                              "4 - To know how to use the Sanila's bots\n"
                              "5 - Sanila's Github Profile\n"
                              "6 - Changelog\n"
                              "7 - Game\n"
                              "8 - Source Code\n\n"
                              "🛑Just send me the number that you want to know\n"
                              "🛑Don't send texts because you won't get correct results")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = telegram.ext.Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(telegram.ext.CommandHandler("start", start_command))
    dp.add_handler(telegram.ext.CommandHandler("help", help_command))

    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
