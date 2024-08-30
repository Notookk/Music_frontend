from pyrogram import Client, filters

@Client.on_message(filters.command('pause') & filters.user('YOUR_ADMIN_ID'))
async def pause(client, message):
    # Code to pause the music on the web
    await message.reply_text("Music paused.")
