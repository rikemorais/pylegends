import os
from typing import Any, Dict

import pandas as pd
from pymongo import MongoClient


class MongoDBConnector:
    """A class for connecting to MongoDB and writing data to a specified collection."""

    def __init__(self) -> None:
        """Initializes the connection to MongoDB using the provided connection string."""
        self.client = None
        self.connection_string = os.getenv("MONGODB_CONNECTION_STRING")

    def run(self, db_name: str, collection_name: str, file_path: str, unique_key_name: str) -> None:
        """Runs the MongoDB loading process."""
        self.connect()
        self.load_data(db_name, collection_name, file_path, unique_key_name)
        self.close()

    def connect(self):
        """Establishes connection to MongoDB using the connection string."""
        if self.connection_string is None:
            raise ValueError("MONGODB_CONNECTION_STRING environment variable is not set.")
        self.client = MongoClient(self.connection_string)

    def close(self):
        """Closes the connection to MongoDB."""
        if hasattr(self, "client"):
            self.client.close()

    def write_data(self, db_name: str, collection_name: str, data: Dict[str, Any], key: Dict[str, Any]) -> None:
        """Overwrites data in the specified MongoDB collection if the document with the given key exists,
        otherwise inserts a new document."""
        db = self.client[db_name]
        collection = db[collection_name]
        collection.replace_one(key, data, upsert=True)

    def load_data(self, db_name: str, collection_name: str, file_path: str, unique_key_name: str) -> None:
        """Loads data from a CSV file into the specified MongoDB collection, overwriting existing documents.

        Args:
            db_name (str): The name of the database.
            collection_name (str): The name of the collection.
            file_path (str): The file path of the CSV to load.
            unique_key_name (str): The name of the unique key in the CSV file.
        """
        data = pd.read_csv(file_path)
        records = data.to_dict(orient="records")

        for record in records:
            key = {unique_key_name: record[unique_key_name]}
            self.write_data(db_name, collection_name, record, key)

        print(f"✅ Data Successfully Loaded into the Collection {collection_name.upper()}!")
