from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RDXMUSIC import app
from config import BOT_USERNAME
from RDXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ Wєʟᴄᴏᴍᴇ Ғᴏʀ ꝛᴅꭙ ʀєᴘᴏs ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/+RObRa7kXPIJmMjU1"),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id="1777270311"),
          ],
               [
                InlineKeyboardButton("ʟɪᴠᴇ ᴄᴄ", url="https://t.me/+RObRa7kXPIJmMjU1"),

],
[
              InlineKeyboardButton("ʙᴀɴ ᴀʟʟ", url=f"https://github.com/RDX-RAj/RDXBANALL"),
              InlineKeyboardButton("︎ꝛᴅꭙ ᴍᴜsɪᴄ", url=f"https://github.com/RDX-RAj/RDXMUSIC"),
              ],
              [
              InlineKeyboardButton("ᴍᴀɴᴀɢᴇᴍᴇɴᴛ", url=f"https://github.com/RDX-RAj/RDXROBOT"),
InlineKeyboardButton("ᴄʜᴀᴛ ʙᴏᴛ", url=f"https://github.com/RDX-RAj/RDXCHATBOT"),
],
[
InlineKeyboardButton("sᴛʀɪɴɢ ʙᴏᴛ", url=f"https://github.com/RDX-RAj/RDXSTRINGBOT"),
InlineKeyboardButton("ᴄʜᴀᴛɢᴘᴛ", url=f"https://github.com/RDX-RAj/RDXCHATGPT"),
],
[
              InlineKeyboardButton("ᴠᴘs", url=f"https://github.com/RDX-RAj/Kaali-Linux"),
              InlineKeyboardButton("ᴍᴏᴠɪᴇ", url=f"https://github.com/RDX-RAj/RDXMOVIEBOT"),
              ],
              [
              InlineKeyboardButton("sᴛʀɪɴɢ ʜᴀᴄᴋ︎", url=f"https://github.com/RDX-RAj/RDXSTRINGHACK"),
InlineKeyboardButton("ɪᴅ ᴄʜᴀᴛ ʙᴏᴛ", url=f"https://github.com/RDX-RAj/RDXIDCHAT"),
],
[
InlineKeyboardButton("ᴜsᴇʀʙᴏᴛ", url=f"https://github.com/RDX-RAj/RDXUSERBOT"),
InlineKeyboardButton("sᴇᴀʀᴄʜ ʙᴏᴛ", url=f"https://github.com/RDX-RAj/SEARCH_BOT"),
],
[
InlineKeyboardButton("ᴄᴄ ʙᴏᴛ", url=f"https://github.com/RDX-RAj/CC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/c785871bcc715f3b399c4.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/DAXXMUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/RDX-RAj/RDXMUSIC) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/+RObRa7kXPIJmMjU1)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


