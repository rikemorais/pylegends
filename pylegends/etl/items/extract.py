import json
import os
from typing import Dict

import pandas as pd
import requests

from pylegends.common.version import get_latest_version
from pylegends.utils.config import LocalPathItens


class ExtractItems:
    """
    Class responsible for extracting information from Riot API items.

    This class makes requests to the game's API to obtain the latest item data and saves it in a JSON file.
    """

    def __init__(self):
        """Initializes the class with the desired version of the item data."""
        self.base_url = "https://ddragon.leagueoflegends.com/cdn/{}/data/pt_BR/item.json"
        self.version = get_latest_version()

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
            Dict: A dictionary with the champions' data, or an empty dictionary if there is a failure.
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
             dict: dictionary containing item data.
        """
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(f"⛔ Error when fetching item data: {response.status_code}")

    @staticmethod
    def save_to_csv(df: pd.DataFrame, filepath: str = LocalPathItens.RAW) -> None:
        """
        Saves the DataFrame to a CSV file.

        Args:
            df (pd.DataFrame): DataFrame containing champions data.
            filepath (str): File path where the data will be saved.
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False, sep=",")
