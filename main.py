from multiprocessing.process import name

import telegram.ext

from telegram.ext import updater

import Constents as keys
import Responses as R

print("Bot Started.....")

def start_command(update, context):
    update.message.reply_text(f"Hi {name},\nWelcome to Sanila Ranatunga's Official Assistant bot🤗🔥/help")

def help_command(update, context):
    update.message.reply_text("I can help you to connect with Sanila within seconds\n\n"
                              "1 - About Bot\n"
                              "2 - About Sanila\n"
                              "3 - Changelog\n"
                              "4 - Game\n"
                              "5 - Github\n"
                              "6 - Feedback\n"
                              "7 - Report Bugs\n"
                              "8 - Help Centre\n\n"
                              "🛑Just send me the number that you want to know\n"
                              "🛑Don't send texts because you won't get correct results")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)




def main():
    updater = telegram.ext.Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(telegram.ext.CommandHandler("start", start_command))
    dp.add_handler(telegram.ext.CommandHandler("help", help_command))

    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))



    updater.start_polling()
    updater.idle()


main()