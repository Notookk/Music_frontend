# utils/permissions.py
from functools import wraps
from pyrogram.types import Message

def admin_required(func):
    """
    Decorator to ensure the user is an admin.

    Args:
        func (function): The function to wrap.

    Returns:
        function: The wrapped function with admin check.
    """
    @wraps(func)
    async def wrapper(client, message: Message):
        if message.from_user.id in get_admin_ids(message.chat.id):
            return await func(client, message)
        else:
            await message.reply_text("You are not authorized to use this command.")
    return wrapper

def get_admin_ids(chat_id):
    """
    Get a list of admin IDs for a chat.
    This is a placeholder function; replace it with actual fetching logic.

    Args:
        chat_id (int): The chat ID to get admins for.

    Returns:
        list: A list of admin user IDs.
    """
    # Placeholder: Replace with actual logic to fetch admin IDs from a database or API
    return [123456789, 987654321]  # Example admin user IDs
