from pyrogram import Client, filters
from pyrogram.types import Message

# Help command to show available bot commands
@Client.on_message(filters.command("help") & filters.private)
async def help(client: Client, message: Message):
    help_text = (
        "Here are the available commands:\n"
        "/help - Show this help message\n"
        "/play <song_name> - Play a song\n"
        "/skip - Skip the current song\n"
        "/stop - Stop playing\n"
        "/pause - Pause the music\n"
    )
    await message.reply_text(help_text)
