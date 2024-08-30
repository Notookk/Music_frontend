from pyrogram import Client, filters
from pyrogram.types import Message

# Start command to welcome new users
@Client.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    start_text = "Welcome to the bot! Use /help to see available commands."
    await message.reply_text(start_text)
