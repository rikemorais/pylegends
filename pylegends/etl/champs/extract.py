import os
from typing import Dict
from pylegends.common.version import get_latest_version
import pandas as pd
import requests

from pylegends.utils.config import LocalPathChamps


class ExtractChamps:
    """
    Class responsible for extracting information from Riot API Champions.

    This class makes requests to the game's API to get the latest champion data and saves it to a CSV file.

    Attributes:
        base_url (str): base URL for the Champions Data API.
        version (str): latest version of the game obtained from the Versions API.
    """

    def __init__(self) -> None:
        """
        Initializes the ExtractChamps Class, setting the base URL and getting the latest version of the game.
        """
        self.base_url = "https://ddragon.leagueoflegends.com/cdn/{}/data/pt_BR/champion.json"
        self.version = get_latest_version()

    def run(self) -> None:
        """
        Runs the champion data extraction process.

        Fetches the data, converts it to a DataFrame and saves it to a CSV file.
        """
        data = self.fetch_data()
        if data:
            df = self.to_dataframe(data)
            self.save_to_csv(df)
            print("✅ Champion Data Saved Successfully!")
        else:
            print("⛔ Failed to Get Champion Data!!!")

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

    @staticmethod
    def to_dataframe(champs_data: Dict) -> pd.DataFrame:
        """
        Converts Champions data into a Pandas DataFrame.

        Args:
            champs_data (Dict): Dictionary containing Champion data.

        Returns:
            pd.DataFrame: DataFrame containing champions data.
        """
        champions = []
        for champ_key, champ_info in champs_data.items():
            champion = {
                "champ_key": champ_key,
                "id": champ_info["id"],
                "key": champ_info["key"],
                "name": champ_info["name"],
                "title": champ_info["title"],
                **champ_info["info"],
                "tags": champ_info["tags"],
                "partype": champ_info["partype"],
                **champ_info["stats"],
            }
            champions.append(champion)
        return pd.DataFrame(champions)

    @staticmethod
    def save_to_csv(df: pd.DataFrame, filepath: str = LocalPathChamps.RAW) -> None:
        """
        Saves the DataFrame to a CSV file.

        Args:
            df (pd.DataFrame): DataFrame containing champions data.
            filepath (str): File path where the data will be saved.
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False, sep=",")
