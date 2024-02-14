from pylegends.common.mongodb import MongoDBConnector
from pylegends.utils.config import LocalPathItems


class LoadItems:
    """Class for loading data into MongoDB 'champs' collection."""

    @staticmethod
    def run() -> None:
        """Loads data from a CSV file into the 'items' collection."""
        loader = MongoDBConnector()
        loader.connect()
        loader.load_data(
            "pylegends",
            "items",
            LocalPathItems.RAW,
            "name",
        )
        loader.close()


if __name__ == "__main__":
    LoadItems().run()
