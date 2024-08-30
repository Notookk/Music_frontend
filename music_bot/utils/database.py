# utils/database.py

def is_on_off(feature_id):
    """
    Check if a feature is enabled or disabled.
    This is a placeholder function; replace it with actual database checks.

    Args:
        feature_id (str): The ID of the feature to check.

    Returns:
        bool: True if the feature is enabled, False otherwise.
    """
    # Placeholder: Check the database for the feature status
    enabled_features = ["play", "pause", "skip", "stop"]
    return feature_id in enabled_features

def get_config(key):
    """
    Get configuration settings from the database or a config file.
    This is a placeholder function; replace it with actual fetching logic.

    Args:
        key (str): The configuration key to retrieve.

    Returns:
        any: The value of the configuration key.
    """
    # Placeholder: Replace with actual database or config file fetching logic
    config = {
        "feature_enabled": True,
        "max_song_duration": 300  # Example: max song duration in seconds
    }
    return config.get(key)
