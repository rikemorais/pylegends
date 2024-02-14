from pylegends.etl.items.extract import ExtractItems
from pylegends.etl.items.load import LoadItems
from pylegends.etl.items.transform import TransformItems


class TaskItems:
    """
    Class responsible for managing and performing data transformation tasks for items.

    This class serves as an orchestrator for the ETL (Extract, Transform, Load) process of item data, calling the
    extraction and transformation classes to perform their respective steps in the data pipeline.
    """

    def __init__(self) -> None:
        """Initializes the instance of the TaskItems class."""
        pass

    @staticmethod
    def run() -> None:
        """
        Performs all ETL tasks for item data.

        Starts the ETL process by executing, in sequence, the data extraction and transformation steps.
        Tasks are performed in an order that ensures correct data manipulation and preparation.
        """
        ExtractItems().run()
        TransformItems().run()
        LoadItems().run()
