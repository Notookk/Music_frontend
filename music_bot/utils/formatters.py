# utils/formatters.py
import re

def time_to_seconds(time_str):
    """
    Convert a time string in the format 'HH:MM:SS' to total seconds.

    Args:
        time_str (str): The time string to convert.

    Returns:
        int: The total number of seconds, or 0 if the input is invalid.
    """
    try:
        parts = list(map(int, re.split('[:]', time_str)))
        return sum(x * 60 ** i for i, x in enumerate(reversed(parts)))
    except (ValueError, TypeError):
        # Return 0 if there's an error in conversion
        return 0
