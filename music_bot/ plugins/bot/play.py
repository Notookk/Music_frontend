from pyrogram import Client, filters
from utils.youtube import YouTubeAPI

yt = YouTubeAPI()

@Client.on_message(filters.command('play') & filters.private)
async def play(client, message):
    query = ' '.join(message.command[1:])
    video = await yt.search_video(query)
    if video:
        url = yt.base_url + video['id']
        file_path = await yt.download_audio(url)
        await message.reply_text(f"Playing: {video['title']}", quote=True)
        # Code to stream the audio to the web goes here
