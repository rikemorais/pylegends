from pylegends.common.mongodb import MongoDBConnector
from pylegends.utils.config import LocalPathChamps


class LoadChamps:
    """Class for loading data into MongoDB 'champs' collection."""

    @staticmethod
    def run() -> None:
        """Loads data from a CSV file into the 'champs' collection."""
        loader = MongoDBConnector()
        loader.connect()
        loader.load_data(
            "pylegends",
            "champs",
            LocalPathChamps.CLEAN,
            "key",
        )
        loader.close()


if __name__ == '__main__':
    LoadChamps().run()
