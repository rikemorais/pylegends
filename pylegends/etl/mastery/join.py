import os

import pandas as pd

from pylegends.utils.config import LocalPathChamps, LocalPathMastery


class JoinChamps:
    """
    Class for joining mastery data and champion information into a single DataFrame.

    The class reads two CSV files, one containing mastery data and the other containing champion information, and joins
    them into a single CSV file. It also organizes the columns of the resulting DataFrame.

    Attributes:
        file1 (str): path to the CSV file containing mastery data.
        file2 (str): path to the CSV file containing champion information.
        output_file (str): path to the output CSV file after joining the data.
    """

    def __init__(self) -> None:
        """Initializes the class with the input and output file paths."""
        self.file1 = LocalPathMastery.CLEAN
        self.file2 = LocalPathChamps.CLEAN
        self.output_file = LocalPathMastery.FINAL

    def run(self) -> None:
        """Performs data joining and column organization processes."""
        self.join_data()
        self.sort_columns()
        print("✅ Join Mastery and Champion Data Saved Successfully!")

    def join_data(self) -> None:
        """Merge mastery data and champion information into a single DataFrame and save it to a CSV file."""
        df1 = pd.read_csv(self.file1)
        df2 = pd.read_csv(self.file2)
        joined_df = pd.merge(df1, df2, on="key", how="inner", validate="many_to_many")
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        joined_df.to_csv(self.output_file, index=False)

    def sort_columns(self) -> None:
        """Arranges the columns of the unified DataFrame and saves changes to the CSV file."""
        df = pd.read_csv(self.output_file)
        specific_columns = [
            "rank",
            "key",
            "champion",
            "title",
            "level",
            "tags",
            "points",
            "last",
            "next",
            "chest",
            "tokens",
            "final",
        ]
        specific_columns = [col for col in specific_columns if col in df.columns]
        other_columns = sorted(col for col in df.columns if col not in specific_columns)
        sorted_columns = specific_columns + other_columns
        df = df[sorted_columns]
        df.to_csv(self.output_file, index=False)
