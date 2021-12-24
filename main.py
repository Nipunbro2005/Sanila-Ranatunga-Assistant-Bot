from multiprocessing.process import name

import telegram.ext

from telegram.ext import updater

import Constents as keys
import Responses as R

print("Bot Started.....")


def start_command(update, context):
    update.message.reply_text("𝐒𝐚𝐧𝐢𝐥𝐚'𝐬 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐁𝐨𝐭\n\n" \
                              "🙋‍♂Hello Fr" \
                              "iends , This is Sanila's Telegram Assistant bot™." \
                              " This bot " \
                              "was created to collect your feedbacks, bugs and ideas about Sanila's bots😊. /help" \
                              "\n\nThese are the bots that created by Sanila🙇‍♂" \
                              ".\n\n▬▬▬▬ ◈ @so" \
                              "ngdownload597_bot" \
                              "\n▬▬" \
                              "▬▬ ◈ @tor" \
                              "rentdownloader88_bot" \
                              "\n" \
                              "▬▬▬" \
                              "▬ ◈ @useful_powerfu" \
                              "l_chat_bot" \
                              "\n▬▬▬▬ ◈ @yout" \
                              "ubevideodownloader45_bot" \
                              "\n\n✨𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬\n" \
                              "\n➥  Sanila " \
                              "Ranatunga" \
                              "\n\n𝟸𝟶𝟸𝟷-𝟸𝟶𝟸𝟸©")


def help_command(update, context):
    update.message.reply_text("✍️Hello dear,"
                              "\n\n🌺You Can Contact Sanila Using This BOT 💁‍♂\n========================\n\n"
                              "1 - About Sanila\n"
                              "2 - Changelog\n"
                              "3 - Github\n"
                              "4 - Feedback\n"
                              "5 - Report Bugs\n"
                              "6 - Bot help Centre\n"
                              "========================\n\n"
                              "⚠Just send me the number that you want to know\n"
                              "⚠Don't send texts because you won't get correct results")


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
