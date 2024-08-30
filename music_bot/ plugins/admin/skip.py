from pyrogram import Client, filters
from pyrogram.types import Message
from utils.permissions import admin_required
from utils.player import MusicPlayer
from flask_socketio import emit

# Skip command to skip the current song for admins
@Client.on_message(filters.command("skip") & filters.group)
@admin_required
async def skip(client: Client, message: Message):
    chat_id = message.chat.id
    if not MusicPlayer.is_playing(chat_id):
        await message.reply_text("No song is currently playing.")
        return

    MusicPlayer.skip(chat_id)
    emit('skip', {'chat_id': chat_id}, namespace='/music')
    await message.reply_text("Skipped the current song!")
