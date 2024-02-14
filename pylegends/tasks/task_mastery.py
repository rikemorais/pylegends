from pylegends.etl.mastery.extract import ExtractMastery
from pylegends.etl.mastery.join import JoinChamps
from pylegends.etl.mastery.load import LoadMastery
from pylegends.etl.mastery.transform import TransformMastery


class TaskMastery:
    """
    Class responsible for managing and performing mastery data transformation tasks.

    Acts as an orchestrator for various ETL (Extract, Transform, Load) tasks for League of Legends mastery data,
    triggering specific ETL classes for each step and ensuring efficient execution of each transformation process.
    """

    def __init__(self) -> None:
        """Initializes the instance of the TaskMastery class."""
        pass

    @staticmethod
    def run() -> None:
        """
        Performs all ETL tasks for mastery data.

        Calls the ETL classes responsible for extracting, transforming and joining mastery data, executing the tasks in
        a logical sequence to ensure correct manipulation and preparation of data for later use.
        """
        ExtractMastery().run()
        TransformMastery().run()
        JoinChamps().run()
        LoadMastery().run()
