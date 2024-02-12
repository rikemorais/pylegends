from typing import Optional, Tuple

import pandas as pd
from pylegends.utils.config import LocalPathMastery


class TransformMastery:
    """
    Class for transforming League of Legends mastery data.

    Reads a CSV file of raw mastery data, applies transformations such as deleting and renaming columns, calculating new
    columns and saving it to another CSV.

    Attributes:
        dataframe (Optional[pd.DataFrame]): DataFrame for transformation.
        file_path (str): Raw data CSV file path.
        columns_to_drop (list[str]): Columns to exclude from the DataFrame.
    """

    def __init__(self) -> None:
        """Initializes the class with settings for data transformation."""
        self.dataframe: Optional[pd.DataFrame] = None
        self.file_path = LocalPathMastery.RAW
        self.columns_to_drop = ["puuid", "summonerId", "championPointsSinceLastLevel"]

    def run(self) -> Tuple[Optional[pd.DataFrame], str]:
        """
        Performs data transformation: loads CSV, deletes/renames columns, calculates new columns and saves the new
        DataFrame.

        Returns:
            Tuple[Optional[pd.DataFrame], str]: Transformed DataFrame and status message.
        """
        if self.load_csv(self.file_path) and self.drop_columns(self.columns_to_drop):
            self.rename_columns()
            self.calculate_final()
            self.converter_timestamp()
            self.create_rank_column()
            save_status = self.save_csv(LocalPathMastery.CLEAN)
            return self.dataframe, "✅ Success!" if save_status else "⛔ Error saving!!!"
        return None, "⛔ Error loading file or deleting columns!!!"

    def load_csv(self, file_path: str) -> bool:
        """Load CSV file into DataFrame. Returns True if successful, False otherwise."""
        try:
            self.dataframe = pd.read_csv(file_path)
            return True
        except FileNotFoundError:
            print(f"⛔ File not found: {file_path}")
            return False

    def drop_columns(self, columns: list[str]) -> bool:
        """Deletes specified columns from the DataFrame. Returns True if successful, False otherwise."""
        if self.dataframe is not None:
            self.dataframe.drop(columns=columns, inplace=True, errors="ignore")
            return True
        else:
            print("⛔ Dataframe not loaded!!!")
            return False

    def rename_columns(self) -> None:
        """Renames DataFrame columns according to defined mapping."""
        if self.dataframe is not None:
            column_mapping = {
                "championId": "key",
                "championLevel": "level",
                "championPoints": "points",
                "lastPlayTime": "last",
                "championPointsSinceLastLevel": "since",
                "championPointsUntilNextLevel": "next",
                "chestGranted": "chest",
                "tokensEarned": "tokens",
            }
            self.dataframe.rename(columns=column_mapping, inplace=True)
        else:
            print("⛔ Dataframe not loaded!!!")

    def calculate_final(self) -> None:
        """Calculates the 'final' column based on specific rules."""
        if self.dataframe is not None:
            self.dataframe["final"] = self.dataframe.apply(self.calculate_final_row, axis=1)

    @staticmethod
    def calculate_final_row(row: pd.Series) -> int:
        """Helper to calculate 'final' for each line. Returns calculated value."""
        return 0 if row["level"] >= 5 else 21600 - row["points"]

    def converter_timestamp(self) -> None:
        """Converts 'last' to datetime format."""
        if self.dataframe is not None:
            self.dataframe["last"] = pd.to_datetime(self.dataframe["last"], unit="ms")
        else:
            print("⛔ Dataframe not loaded!!!")

    def create_rank_column(self) -> None:
        """Create 'ranking' column based on 'level 'points'."""
        if self.dataframe is not None:
            self.dataframe.sort_values(by=["level", "points"], ascending=[False, False], inplace=True)
            self.dataframe["rank"] = (
                self.dataframe[["level", "points"]].apply(tuple, axis=1).rank(method="first", ascending=False)
            )
        else:
            print("⛔ Dataframe not loaded!!!")

    def save_csv(self, save_path: str) -> bool:
        """Saves DataFrame to CSV. Returns True if successful, False otherwise."""
        if self.dataframe is not None:
            try:
                self.dataframe.to_csv(save_path, index=False)
                return True
            except Exception as e:
                print(f"⛔ Error saving file: {e}")
                return False
        else:
            print("⛔ There is no dataframe to save!!!")
            return False
