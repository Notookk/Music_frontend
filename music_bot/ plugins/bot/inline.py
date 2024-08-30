from pyrogram import Client, filters
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from utils.youtube import YouTubeAPI

yt = YouTubeAPI()

@Client.on_inline_query()
async def inline_query_handler(client: Client, inline_query: InlineQuery):
    query = inline_query.query.strip()
    if not query:
        await inline_query.answer(
            results=[],
            cache_time=1
        )
        return

    video = await yt.search_video(query)
    if video:
        title = video['title']
        url = yt.base_url + video['id']
        description = f"Click to play {title}"

        result = [
            InlineQueryResultArticle(
                title=title,
                description=description,
                input_message_content=InputTextMessageContent(f"/play {url}"),
                thumb_url=video['thumbnails'][0]['url']
            )
        ]

        await inline_query.answer(
            results=result,
            cache_time=1
        )
