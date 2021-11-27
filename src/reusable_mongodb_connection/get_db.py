from typing import Optional

from pymongo import MongoClient
from pymongo.errors import OperationFailure

from reusable_mongodb_connection.types import MongoDBURI
from reusable_mongodb_connection.exceptions import ReusableMongodbConnectionError


def get_db(url: MongoDBURI, database: Optional[str] = None):
    # check that connected
    try:
        client = MongoClient(url, serverSelectionTimeoutMS=5000)

        # check that connection is available
        client.server_info()

        db = client.get_default_database(database)

        return db
    except OperationFailure:
        raise ReusableMongodbConnectionError(
            f"can't connect to database `{database}` via url `{url}`"
        )
