from pyrogram import Client, filters

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text("Welcome to the Music Bot! Use /play <song name> to play music.")
