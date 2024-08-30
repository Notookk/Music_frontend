from pyrogram import Client, filters
from pyrogram.types import Message
from flask_socketio import emit

# Play command to start music playback
@Client.on_message(filters.command("play") & filters.group)
async def play(client: Client, message: Message):
    chat_id = message.chat.id
    song_name = message.text.split(' ', 1)[1] if len(message.text.split()) > 1 else 'default song'
    emit('play', {'chat_id': chat_id, 'song': song_name}, namespace='/music')
    await message.reply_text(f"Playing the song: {song_name}!")
