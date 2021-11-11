from typing import Optional

from pymongo import MongoClient
from reusable_mongodb_connection.types import MongoDBURI


def get_db(url: MongoDBURI, database: Optional[str]):
    # check that connected
    try:
        client = MongoClient(url, serverSelectionTimeoutMS = 5000)
        
        # check that connection is available
        client.server_info()

        db = client.get_default_database(database)
        
        return db
    except:
        raise Exception(f"can't connect to {database}@{url}")
