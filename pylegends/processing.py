from pylegends.tasks.task_champs import TaskChamps
from pylegends.tasks.task_items import TaskItems
from pylegends.tasks.task_mastery import TaskMastery


class Processing:
    """
    Class responsible for coordinating Riot API data processing.

    This class orchestrates the execution of various data processing tasks, including data transformation, joining,
    quality checking, and storage.
    """

    @staticmethod
    def run() -> None:
        """
        Runs the full Riot API processing pipeline.

        Performs a series of tasks to process API data, including data transformation, joining, quality checks, and
        other necessary steps.
        """
        try:
            TaskChamps().run()
            TaskMastery().run()
            TaskItems().run()

        except Exception as e:
            print(f"An error occurred while processing the Data: {e}")
            raise
