from pyrogram import Client, filters

@Client.on_message(filters.command("help") & filters.private)
async def help(client, message):
    help_text = """
    **Music Bot Commands:**
    
    /start - Start the bot
    /help - Show help information
    /play [song name] - Play a song
    /pause - Pause the music (Admin only)
    /skip - Skip the current song (Admin only)
    /stop - Stop the music (Admin only)
    """
    await message.reply_text(help_text)
