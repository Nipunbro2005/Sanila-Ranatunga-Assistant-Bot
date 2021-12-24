from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("1"):
        return "𝗔𝗯𝗼𝘂𝘁 𝗦𝗮𝗻𝗶𝗹𝗮\n\n" \
               "❖ Name : Sanila Ranatunga😎\n\n" \
               "❖ Age : 14 Years (2021) 🙃\n\n" \
               "❖ Birthday : 09.01.2007 (2021)\n\n" \
               "❖ From : Sri Lanka🇱🇰\n\n" \
               "❖ Skills : Programmer , Developer😏\n\n" \
               "❖ Ambition : Be a software engineer😊\n\n" \
               "❖ Programming Languages : Python, HTML🙃\n"

    if user_message in ("2"):
        return "𝐂𝐡𝐚𝐧𝐠𝐞𝐥𝐨𝐠\n\n" \
               "🆅0.6\n" \
               " -Fixed errors in v0.5\n" \
               " -Made much easier to use\n" \
               " -Changed the welcome msg\n" \
               " -Removed the game\n\n" \
               "🆅0.5\n" \
               " -Bug fixes and optimizations\n\n" \
               "🆅0.4\n" \
               " -Fixed problem in game\n" \
               " -Changed the interface\n\n" \
               "🆅0.3\n" \
               " -Added time (US Time)\n\n" \
               "🆅0.2\n" \
               " -Changed the interface much attractive\n" \
               " -What's new changed to Changelog\n" \
               " -Fixed problem in 12 (Song downloader)\n" \
               " -Added time also\n" \
               " -Minor bugs fixes\n\n" \
               "🆅0.1\n" \
               " -Added Some Commands\n" \
               " -Made much easier to use\n" \
               " -Improved Chat Facilities\n"

    if user_message in ("3"):
        return "Here's the github profile👇\n\nhttps://github.com/sanila2007"

    if user_message in ("4"):
        return "Don't be shy, send me your feedback❤"

    if user_message in ("5"):
        return "Send me your problem. Your bugs reports helps a " \
               "lot to make those very powerful."

    if user_message in ("6"):
        return "Bot help Centre\n\n" \
               "10 - How to use the bots\n" \
               "11 - Not Responding error in bots\n" \
               "12 - Always receiving error messages in bots\n\nChoose your problem and send me the number🔥"

    if user_message in ("10"):
        return "13 - Youtube Video Download Bot\n" \
               "14 - Torrent Downloader Bot\n" \
               "15 - Song Downloader Bot\n" \
               "16 - Chat bot\n\n" \
               "Choose the bot and send me the number"

    if user_message in ("11"):
        return "That will be a problem in server. We will settle that problem soon. Thank you❤"

    if user_message in ("12"):
        return "Try again after 1 day and it will be automatically settled😉"

    if user_message in ("13"):
        return "Youtube Video Downloader🎞\n\n" \
               "⭕️First use /start command in @youtubevideodownloader45_bot\n\n" \
               "⭕Second send the url of the video that you need to download.\n\n" \
               "⭕️Next you will receive some buttons that shows the quality and select the quality.\n\n" \
               "⭕️Finally you will receive a message that VIDEO or Document. Select each one and wait for a moment and " \
               "you will receive a video.\n\n" \
               "Let's enjoy your video🤗\n\nHere's the bot👇👇\nhttps://t.me/youtubevideodownloader45_bot"

    if user_message in ("14"):
        return "Torrent Downloader🎥\n\n" \
               "⭕️First use /start command in @torrentdownloader88_bot\n\n" \
               "⭕️Second click the inline button. Either yts or else what you want.\n\n" \
               "⭕️Next type the movie name and select the correct movie.\n\n" \
               "⭕️Finally you will receive a torrent file link and click on it and download.\n\n" \
               "Enjoy🤗\n\nHere's the bot👇👇\nhttps://t.me/torrentdownloader88_bot"

    if user_message in ("15"):
        return "Song Download Bot🎵\n\n" \
               "⭕️First click the /start command in @songdownload597_bot\n\n" \
               "⭕️Second send me the song name. Don't only send the song name. You must send it like this Eg: /song " \
               "faded\n\n" \
               "Enjoy your song🤗\n\nHere's the " \
               "bot👇\nhttps://t.me/songdownload597_bot "

    if user_message in ("16"):
        return "Chat Bot Advance📝\n\n" \
               "⭕️First use /start command in @useful_powerful_chat_bot\n\n" \
               "⭕️Second click the /help command and you will receive a msg that how to use that bot.\n\n" \
               "Enjoy your Chat Bot🤗\n\nHere's the bot👇\nhttps://t.me/useful_powerful_chat_bot"


    if user_message in ("time", "time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Please wait a While🚶‍♂\n\nYour msg has been sent to Sanila✨"
