from pyrogram import filters, Client
from pyrogram.types import Message
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

logo = Client("logo Bot", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)


caption = """
āļø ššØš šØ šš«ššš­šš šš®ššš¬š¬šš®š„š„š² ā
āāāāāāāāāāāāāāāāā

š **š¾š§ššš©šš š½š®** : **[ššØš šØ ššš§šš«šš­š ššØš­ š§āš»](https://t.me/LogoGeneratorRymBot)**

šŗ **ššš¦šŖššØš©šš§** : ** {} **

š **šš¤š¬šš§š š½š®**  : **[š„ šš²š¦ šššš¢šš¢šš„ š„](https://t.me/RymOfficial)**
āāāāāāāāāāāāāāāāāļø  
    """
#āāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāā 

#āāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāā 

@logo.on_message(filters.command("start"))
async def start(client,message):
    await message.reply_chat_action("typing")
    await message.reply_photo(photo="https://telegra.ph/file/859bfec6a5ba66df9d64b.jpg", caption="š šš š š¼š¢ šš®š¢ šš¤šš¤ ššš£šš§šš©š¤š§ š½š¤š© šš¤š§ ššš”ššš§šš¢ \n\nš½š® @RymBots š¾š§ššš©šš š½š® @TumaraBaap...\n\nš¾š¤š¢š¢šš£ššØ - /logo, /logohq, /wall, /write")


#āāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāā 

@logo.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š šš©šš§ šš§ ššØšØš š„š š", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "š ššØš¢š§ šššš¢šš¢šš„ šš”šš§š§šš„ š", url="https://t.me/RymOfficial"
                    )
                ]
            ]
          ),
    )

#āāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāā 
  
@logo.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/logohq?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š šš©šš§ šš§ ššØšØš š„š š", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "š ššØš¢š§ šššš¢šš¢šš„ šš”šš§š§šš„ š", url="https://t.me/RymOfficial"
                    )
                ]
            ]
          ),
    )

#āāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāā 


@logo.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/wallpaper?search={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š šš©šš§ šš§ ššØšØš š„š š", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "š ššØš¢š§ šššš¢šš¢šš„ šš”šš§š§šš„ š", url="https://t.me/RymOfficial"
                    )
                ]
            ]
          ),
    )

#āāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāāā 


@logo.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/write?write={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š šš©šš§ šš§ ššØšØš š„š š", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "š ššØš¢š§ šššš¢šš¢šš„ šš”šš§š§šš„ š", url="https://t.me/RymOfficial"
                    )
                ]
            ]
          ),
    )


logo.run()

app.start()
LOGGER.info("Ā© @TumaraBaap")
idle()
