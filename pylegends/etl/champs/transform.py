from typing import List, Optional, Tuple

import pandas as pd

from pylegends.utils.config import LocalPathChamps


class TransformChamps:
    """Class responsible for transforming data from League of Legends Champions.

    Loads data from a CSV file, performs transformations such as deleting and renaming columns, and saves the result to
    a new CSV file.

    Attributes:
        dataframe (pd.DataFrame): DataFrame containing champions data.
        file_path (str): path of the input CSV file.
        columns_to_drop (List[str]): List of columns to exclude from the DataFrame.
    """

    def __init__(self) -> None:
        """Initializes the class with the raw data file path and columns to drop."""
        self.dataframe: Optional[pd.DataFrame] = None
        self.file_path: str = LocalPathChamps.RAW
        self.columns_to_drop: List[str] = [
            "champ_key",
            "id",
            "championPointsSinceLastLevel",
        ]

    def run(self) -> Tuple[Optional[pd.DataFrame], str]:
        """
        Performs the complete data transformation process.

        Load the CSV, delete columns, rename columns, calculate new columns and save the new DataFrame.

        Returns:
            Tuple[Optional[pd.DataFrame], str]: a tuple containing the transformed DataFrame and a status message.
        """
        if self.load_csv(self.file_path) and self.drop_columns(self.columns_to_drop):
            self.rename_columns()

            save_status = self.save_csv(LocalPathChamps.CLEAN)
            if save_status:
                return (
                    self.dataframe,
                    "Dataframe loaded, columns deleted, renamed, and saved successfully!",
                )
            else:
                return (
                    None,
                    "Dataframe loaded, columns deleted, renamed, but there was an error saving!!!",
                )
        return None, "Error loading file or deleting columns!!!"

    def load_csv(self, file_path: str) -> bool:
        """
        Loads the CSV file into a DataFrame.

        Args:
            file_path (str): CSV file path.

        Returns:
            bool: true if the file is loaded successfully, false otherwise.
        """
        try:
            self.dataframe = pd.read_csv(file_path)
            return True
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return False

    def drop_columns(self, columns: List[str]) -> bool:
        """
        Delete specific columns from the DataFrame.

        Args:
            columns (List[str]): List of columns to delete.

        Returns:
            bool: true if the columns are successfully deleted, false otherwise.
        """
        if self.dataframe is not None:
            self.dataframe.drop(columns=columns, inplace=True, errors="ignore")
            return True
        else:
            print("Dataframe Was Not Loaded!!!")
            return False

    def rename_columns(self) -> None:
        """Renames the DataFrame columns according to the defined mapping."""
        if self.dataframe is not None:
            column_mapping = {"name": "champion"}
            self.dataframe.rename(columns=column_mapping, inplace=True)
        else:
            print("Dataframe Was Not Loaded!!!")

    def save_csv(self, save_path: str) -> bool:
        """
        Saves the DataFrame to a CSV file.

        Args:
            save_path (str): Path of the destination CSV file.

        Returns:
            bool: true if the file is saved successfully, false otherwise.
        """
        if self.dataframe is not None:
            try:
                self.dataframe.to_csv(save_path, index=False)
                return True
            except Exception as e:
                print(f"Error saving file: {e}")
                return False
        else:
            print("There is no dataframe to save!!!")
            return False


if __name__ == "__main__":
    transformer = TransformChamps()
    dataframe, message = transformer.run()
    print(message)
