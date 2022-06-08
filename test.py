from pyrogram import client, filters
from pyrogram.type import InlineKeyboardMarkup, InlineKeyboardButton

nihaal=client(
    "Pyrogram Bot",
    bot_token="5541342240:AAFvlATqafF1FB7TtMAMNVqdOv04c1a7nuY",
    api_id="18850696",
    api_hash="e3f5a7b4ea28b5c7ce9fc65e48274ae6"
)

@nihaal.on_message(filters.command("start"))
async def start_message(nihaal,message):
    await message.reply_photo(
        photo="https://telegra.ph/file/3f5c3a461d41522a3b7d2.jpg",
        caption="hello iam just a test bot ",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("owner", url="https://t.me/NL_MP4"),
            InlineKeyboardButton("group", url="https://t.me/movie_lookam")
            ],[
            InlineKeyboardButton("help", callback_data="help"),
            InlineKeyboardButton("about", callback_data="about")
            ]]
         )
    )
        
            
    
    
nihaal.run()
