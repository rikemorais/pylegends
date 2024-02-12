from typing import Optional

import requests


def get_latest_version() -> Optional[str]:
    """
    Gets the latest version of the game from the API.

    Returns:
        Optional[str]: The latest version of the game, or None if the request fails.
    """
    versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    response = requests.get(versions_url)
    versions = response.json()
    return versions[0] if versions else None
