class Riot:
    """
    Constants related to the Riot Games API.

    Stores URLs and identifiers used to make requests to the Riot Games API.

    Attributes:
        URL_CHAMPS (str): Base URL for the Champion Mastery API.
        PUUID (str): Player identifier (PUUID).
    """

    URL_CHAMPS: str = "https://br1.api.riotgames.com/lol/champion-mastery/v4/" "champion-masteries/by-puuid/"
    PUUID: str = "Hj9Nd07B27U2qvJV0VnHira-oC1uliJPeQIzbdR_a1pYJ13_Bon_4ekX4-GNDrIZLXDACvzBvWjVpg"


class LocalPathMastery:
    """
    Local paths to mastery data files.

    Defines paths for raw, clean, and final CSV files related to mastery data.

    Attributes:
        RAW (str): raw CSV file path.
        CLEAN (str): clean CSV file path.
        FINAL (str): path of the final CSV file.
    """

    RAW: str = "data/mastery/raw.csv"
    CLEAN: str = "data/mastery/clear.csv"
    FINAL: str = "data/mastery/final.csv"


class LocalPathChamps:
    """
    Local paths to champion data files.

    Defines paths for raw, clean, and final CSV files related to champion data.

    Attributes:
        RAW (str): raw CSV file path.
        CLEAN (str): clean CSV file path.
    """

    RAW: str = "data/champs/raw.csv"
    CLEAN: str = "data/champs/clean.csv"


class LocalPathItems:
    """
    Local paths to item data files.

    Defines paths for raw, clean, and final CSV files related to item data.

    Attributes:
        RAW (str): Raw CSV file path.
        CLEAN (str): Clean CSV file path.
    """

    RAW: str = "data/items/raw.csv"
    CLEAN: str = "data/items/clean.csv"
