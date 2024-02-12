import os
from typing import Dict, Optional

import pandas as pd
import requests
from pylegends.utils.config import Riot


class ExtractMastery:
    """
    Class to extract champion mastery information for a specific player using the Riot Games API.

    This class makes requests to the Riot Games API to obtain champions' mastery data and saves it to a CSV file.

    Attributes:
        BASE_URL (str): Base URL to access champion mastery data.
        PUUID (str): Player ID (PUUID) for which mastery will be extracted.
        API_KEY (str): Riot Games API Key.
    """

    def __init__(self) -> None:
        """Initializes the class with settings to access the Riot Games API."""
        self.BASE_URL = Riot.URL_CHAMPS
        self.PUUID = Riot.PUUID
        self.API_KEY = os.environ.get("API_KEY")

    def run(self) -> None:
        """
        Performs the process of extracting data from the API, transforming it into a DataFrame and saving it in CSV.
        """
        try:
            response = self.get_champion_mastery()
            if not response:
                raise ValueError("⛔ No Data Returned by API!!!")

            dataframe = self.response_to_dataframe(response)
            self.save_dataframe_to_csv(dataframe)
            print("✅ Mastery Data Saved Successfully!")
        except Exception as err:
            raise Exception(f"⛔ Error During RiotGamesAPI Execution: {err}") from err

    def get_champion_mastery(self) -> Optional[Dict]:
        """
        Get single-player champion mastery from the Riot Games API.

        Returns:
            Optional[Dict]: champion mastery data or None if the request fails.
        """
        url = f"{self.BASE_URL}{self.PUUID}?api_key={self.API_KEY}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"⛔ Error when accessing the API - Status Code: {response.status_code}")
            return None

        return response.json()

    @staticmethod
    def response_to_dataframe(response: Dict) -> pd.DataFrame:
        """
        Converts the API response to a pandas DataFrame.

        Args:
            response (Dict): API response containing champion mastery data.

        Returns:
            pd.DataFrame: DataFrame containing champions' mastery data.
        """
        return pd.DataFrame(response)

    @staticmethod
    def save_dataframe_to_csv(dataframe: pd.DataFrame, filename: str = "raw.csv") -> None:
        """
        Saves the DataFrame to a CSV file.

        Args:
            dataframe (pd.DataFrame): DataFrame to be saved.
            filename (str): Output file name.
        """
        base_path = os.path.join("data", "mastery")
        full_path = os.path.join(base_path, filename)

        if not os.path.exists(base_path):
            os.makedirs(base_path)

        dataframe.to_csv(full_path, sep=",", index=False)
