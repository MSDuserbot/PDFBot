from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey [👋](https://telegra.ph/file/57873ee2279555866f4c9.jpg) {}

Welcome to {}

I can help you to do stuff on PDFs as well as convert images to PDF. Use /help to see features.

JUST SEND A PDF (or an image) to get started.

By @TamilBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ʜᴏᴍᴇ", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/tamilbots")],
        [
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴅᴇᴠ", url="https://t.me/AboutMK")],
    ]

    # Help Message
    HELP = """
**Usage**

1) Just send a PDF to do stuff on it
2) Send images to convert to PDFs

**Functions**
1) Rotate PDF Pages
2) Merge PDFs
3) Encrypt PDFs
4) Decrypt PDFs
5) Convert Images to PDF
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot with PDF Tools by @TamilBots

Source Code : [Click Here](https://github.com/IamBluedragon)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [TamilBotz](t.me/tamilbotz)

Support : [Tamil Supports](t.me/TamilSupport)

Updates : [TamilBots](t.me/tamilbots)
    """
