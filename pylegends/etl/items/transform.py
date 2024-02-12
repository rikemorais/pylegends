import json
import os
from typing import Dict, Optional

import pandas as pd
import requests

from pylegends.utils.config import LocalPathItems


class TransformItems:
    """
    Class responsible for transform information from Riot API items.

    This class makes requests to the game's API to obtain the latest item data and saves it in a JSON file.
    """

    def __init__(self):
        """Initializes the class with the desired version of the item data."""
        self.base_url = "https://ddragon.leagueoflegends.com/cdn/{}/data/pt_BR/item.json"
        self.version = self.get_latest_version()

    def run(self) -> None:
        """Performs the process of extracting data from items."""
        data = self.fetch_data()
        if data:
            df = pd.DataFrame.from_dict(data, orient="index")
            self.save_to_csv(df)
            print("✅ Item Data Saved Successfully!")
        else:
            print("⛔ Failed to Get Item Data!!!")

    def fetch_data(self) -> Dict:
        """
        Fetches champion data using the API.

        Returns:
            Dict: a dictionary with the item data, or an empty dictionary if there is a failure.
        """
        if self.version:
            final_url = self.base_url.format(self.version)
            response = requests.get(final_url)
            data = response.json()
            return data["data"]
        else:
            print("⛔ Unable to Get Latest Version!!!")
            return {}

    def fetch_items(self) -> dict:
        """
        Makes the request to the API and returns the item data.

        Returns:
            dict: Dictionary containing item data.
        """
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"Error when fetching item data: {response.status_code}")

    @staticmethod
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

    @staticmethod
    def save_to_csv(df: pd.DataFrame, filepath: str = LocalPathItems.RAW) -> None:
        """
        Saves the DataFrame to a CSV file.

        Args:
            df (pd.DataFrame): DataFrame containing items data.
            filepath (str): File path where the data will be saved.
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False, sep=",")
