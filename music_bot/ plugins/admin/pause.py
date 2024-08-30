from pyrogram import Client, filters
from pyrogram.types import Message
from utils.permissions import admin_required
from flask_socketio import emit

# Pause command to pause the music for admins
@Client.on_message(filters.command("pause") & filters.group)
@admin_required
async def pause(client: Client, message: Message):
    chat_id = message.chat.id
    emit('pause', {'chat_id': chat_id}, namespace='/music')
    await message.reply_text("Paused the music!")
