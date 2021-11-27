from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("1"):
        return "I'm the Official Assistant Bot of @SanilaRanatunga😎🔥\n\n" \
               "I can help you to solve your problems without connecting with Sanila. /help"

    if user_message in ("2"):
        return "Sometimes @SanilaRanatunga won't either reply or read the messages because " \
               "he always tries to be aware from spam. " \
               "So you have a chance to send me your messages and " \
               "I will send it to Sanila. Later he will reply to your msg soon."

    if user_message in ("3"):
        return "Thanks for using my bots😋❤\n\n" \
               "Send me the problems that you have faced in the bots."

    if user_message in ("4"):
        return "10 - Youtube Video Download Bot\n" \
               "11 - Torrent Downloader Bot\n" \
               "12 - Song Downloader Bot\n" \
               "13 - Chat bot\n\n" \
               "Choose the bot and send me the number"

    if user_message in ("5"):
        return "Here's the github profile👇\n\nhttps://github.com/sanila2007"

    if user_message in ("6"):
        return "Changelog\n\n" \
               "v0.2\n" \
               " -Changed the interface much attractive\n" \
               " -What's new changed to Changelog\n" \
               " -Fixed problem in 12(Song downloader)\n" \
               " -Added time also\n" \
               " -Minor bugs fixes\n\n" \
               "v0.1\n" \
               " -Added Some Commands\n" \
               " -Made much easier to use\n" \
               " -Improved Chat Facilities\n"

    if user_message in ("7"):
        return "Oops....\nThis facility isn't here yet. This will be come in next feature update"

    if user_message in ("8"):
        return "Here's the Source Code👇👇\n\nhttps://github.com/sanila2007/Sanila-Ranatunga-Assistant-Bot"

    if user_message in ("10"):
        return "Youtube Video Downloader🎞\n\n" \
               "⭕️First use /start command in @youtubevideodownloader45_bot\n\n" \
               "⭕Second send the url of the video that you need to download.\n\n" \
               "⭕️Next you will receive some buttons that shows the quality and select the quality.\n\n" \
               "⭕️Finally you will receive a message that VIDEO or Document. Select each one and wait for a moment and " \
               "you will receive a video.\n\n" \
               "Let's enjoy your video🤗\n\nHere's the bot👇👇\nhttps://t.me/youtubevideodownloader45_bot"

    if user_message in ("11"):
        return "Torrent Downloader🎥\n\n" \
               "⭕️First use /start command in @torrentdownloader88_bot\n\n" \
               "⭕️Second click the inline button. Either yts or else what you want.\n\n" \
               "⭕️Next type the movie name and select the correct movie.\n\n" \
               "⭕️Finally you will receive a torrent file link and click on it and download.\n\n" \
               "Enjoy🤗\n\nHere's the bot👇👇\nhttps://t.me/torrentdownloader88_bot"

    if user_message in ("12"):
        return "Song Download Bot🎵\n\n" \
               "⭕️First click the /start command in @songdownload597_bot\n\n" \
               "⭕️Second send me the song name. Don't only send the song name. You must send it like this Eg: /song " \
               "faded\n\n" \
               "Enjoy your song🤗\n\nHere's the " \
               "bot👇\nhttps://t.me/songdownload597_bot "

    if user_message in ("13"):
        return "Chat Bot Advance📝\n\n" \
               "⭕️First use /start command in @useful_powerful_chat_bot\n\n" \
               "⭕️Second click the /help command and you will receive a msg that how to use that bot.\n\n" \
               "Enjoy your Chat Bot🤗\n\nHere's the bot👇\nhttps://t.me/useful_powerful_chat_bot"

    if user_message in ("time", "time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Your message has been sent to @SanilaRanatunga✨"
