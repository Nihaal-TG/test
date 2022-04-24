from pyrogram import client, filters

nihaal=client(
    "Pyrogram Bot",
    bot_token="5189137384:AAEhAxlEn9f9wwMHYNJDvxmW-1PkOHHRlD0",
    api_id="18850696",
    api_hash="e3f5a7b4ea28b5c7ce9fc65e48274ae6"
)

@nihaal.on_message(filters.command("start"))
async def start_message(bot,message):
    await message.reply_text("hi iam just test bot made by @NL_MP4")
    
    
nihaal.run()
