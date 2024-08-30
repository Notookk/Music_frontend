from pyrogram import Client, filters
from pyrogram.types import Message
from utils.permissions import admin_required
from utils.player import MusicPlayer
from flask_socketio import emit

# Stop command to stop the music for admins
@Client.on_message(filters.command("stop") & filters.group)
@admin_required
async def stop(client: Client, message: Message):
    chat_id = message.chat.id
    if not MusicPlayer.is_playing(chat_id):
        await message.reply_text("No song is currently playing.")
        return

    MusicPlayer.stop(chat_id)
    emit('stop', {'chat_id': chat_id}, namespace='/music')
    await message.reply_text("Stopped the music!")
