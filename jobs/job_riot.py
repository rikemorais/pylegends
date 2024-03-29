import time

from pylegends.processing import Processing


class ETLRiot:
    """Class responsible for managing the ETL Process.

    This class encapsulates the ETL process, handles exceptions, and records execution time.

    Attributes:
        etl_process (Processing): An instance of the Processing class to run the ETL process.
    """

    def __init__(self) -> None:
        """Initializes the ETLRiot class and prepares the ETL process."""
        self.etl_process = Processing()

    def run(self) -> None:
        """Runs the ETL process and handles exceptions.

        Starts the ETL process, records the execution time, and handles any exceptions that may occur during the
        process.
        """
        start_time = time.monotonic()

        try:
            self.etl_process.run()
            self._log_success(start_time)

        except Exception as e:
            self._log_failure(e)
            raise

    @staticmethod
    def _log_success(start_time: float) -> None:
        """Records the execution time of the ETL process in case of success.

        Args:
            start_time (float): The start time of the ETL process.
        """
        end_time = time.monotonic()
        elapsed_time = end_time - start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        time_parts = []
        if hours:
            hour_str = "hour" if hours == 1 else "hours"
            time_parts.append(f"{int(hours)} {hour_str}")
        if minutes:
            minute_str = "minute" if minutes == 1 else "minutes"
            time_parts.append(f"{int(minutes)} {minute_str}")
        if seconds or not time_parts:  # Always show seconds if no hours or minutes
            second_str = "second" if seconds == 1 else "seconds"
            time_parts.append(f"{int(seconds)} {second_str}")

        time_str = " ".join(time_parts)
        print(f"✅ Success! Total Execution Time of ETL JOB: 🕒 {time_str}")

    @staticmethod
    def _log_failure(error: Exception) -> None:
        """Logs a failure message in case of an exception during the ETL process.

        Args:
            error (Exception): The exception caught during the execution of the ETL process.
        """
        print(f"⛔ ETL JOB FAILED!!!! Error: {error}")


if __name__ == "__main__":
    etl_job = ETLRiot()
    etl_job.run()
