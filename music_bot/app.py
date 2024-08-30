from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from pyrogram import Client, filters
from utils.player import MusicPlayer
from utils.permissions import admin_required

app = Flask(__name__)
socketio = SocketIO(app)

# Pyrogram Client
bot = Client("my_bot")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('play')
def handle_play(data):
    chat_id = data.get('chat_id')
    song = data.get('song')
    # Add play functionality here using MusicPlayer
    emit('play_ack', {'status': 'playing', 'song': song})

@socketio.on('pause')
def handle_pause(data):
    chat_id = data.get('chat_id')
    # Add pause functionality here using MusicPlayer
    emit('pause_ack', {'status': 'paused'})

@socketio.on('stop')
def handle_stop(data):
    chat_id = data.get('chat_id')
    MusicPlayer.stop(chat_id)
    emit('stop_ack', {'status': 'stopped'})

@socketio.on('skip')
def handle_skip(data):
    chat_id = data.get('chat_id')
    MusicPlayer.skip(chat_id)
    emit('skip_ack', {'status': 'skipped'})

@bot.on_message(filters.command("play"))
async def play_command(client, message):
    song = " ".join(message.command[1:])
    chat_id = message.chat.id
    MusicPlayer.play(chat_id, song)
    await message.reply_text(f"Playing {song}")

@bot.on_message(filters.command("pause") & filters.group)
@admin_required
async def pause_command(client, message):
    chat_id = message.chat.id
    MusicPlayer.pause(chat_id)
    await message.reply_text("Paused")

@bot.on_message(filters.command("stop") & filters.group)
@admin_required
async def stop_command(client, message):
    chat_id = message.chat.id
    MusicPlayer.stop(chat_id)
    await message.reply_text("Stopped")

@bot.on_message(filters.command("skip") & filters.group)
@admin_required
async def skip_command(client, message):
    chat_id = message.chat.id
    MusicPlayer.skip(chat_id)
    await message.reply_text("Skipped")

if __name__ == '__main__':
    bot.start()
    socketio.run(app, host='0.0.0.0', port=5000)
