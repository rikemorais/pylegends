from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from typing import Any, Dict


class MongoDBConnector:
    """Uma classe para conectar-se ao MongoDB e escrever dados em uma coleção.

    Esta classe usa o pymongo para conectar-se a um cluster MongoDB especificado
    e fornece um método para escrever dados em um banco de dados e coleção específicos.

    Attributes:
        connection_string (str): A string de conexão para o cluster MongoDB.
        client (MongoClient): O cliente pymongo conectado ao cluster MongoDB.
    """

    def __init__(self, connection_string: str) -> None:
        """Inicializa a conexão com o MongoDB usando a string de conexão fornecida.

        Args:
            connection_string: A string de conexão para o cluster MongoDB.
        """
        self.connection_string = connection_string
        self.client = MongoClient(self.connection_string)

    def write_data(self, db_name: str, collection_name: str, data: Dict[str, Any]) -> None:
        """Escreve dados na coleção especificada do MongoDB.

        Args:
            db_name: O nome do banco de dados onde os dados serão escritos.
            collection_name: O nome da coleção onde os dados serão escritos.
            data: Um dicionário representando os dados a serem escritos.
        """
        db: Database = self.client[db_name]
        collection: Collection = db[collection_name]
        collection.insert_one(data)
