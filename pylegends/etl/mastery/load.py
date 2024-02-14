from pylegends.common.mongodb import MongoDBConnector
from pylegends.utils.config import LocalPathMastery


class LoadMastery:
    """Class for loading data into MongoDB 'mastery' collection."""

    @staticmethod
    def run() -> None:
        """Loads data from a CSV file into the 'mastery' collection."""
        loader = MongoDBConnector()
        loader.connect()
        loader.load_data(
            "pylegends",
            "mastery",
            LocalPathMastery.FINAL,
            "key",
        )
        loader.close()


if __name__ == "__main__":
    LoadMastery().run()
