from pylegends.etl.champs.extract import ExtractChamps
from pylegends.etl.champs.transform import TransformChamps


class TaskChamps:
    """
    Class responsible for managing and executing data transformation tasks for champions.

    This class serves as an orchestrator for the champions data ETL (Extract, Transform, Load) process, calling the
    extraction and transformation classes to execute their respective steps in the data pipeline.
    """

    def __init__(self) -> None:
        """Initializes the instance of the TaskChamps class."""
        pass

    @staticmethod
    def run() -> None:
        """
        Performs all ETL tasks for champion data.

        Starts the ETL process by executing, in sequence, the data extraction and transformation steps.
        Tasks are performed in an order that ensures correct data manipulation and preparation.
        """
        ExtractChamps().run()
        TransformChamps().run()
