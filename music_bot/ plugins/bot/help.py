from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("help") & filters.private)
async def help(client: Client, message: Message):
    help_text = "Here are the available commands:\n/help - Show this help message\n/play - Play a song\n/skip - Skip the current song\n/stop - Stop playing"
    await message.reply_text(help_text)
