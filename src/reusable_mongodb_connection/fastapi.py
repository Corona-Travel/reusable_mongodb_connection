"""
stuff for fastapi app

keep in mind that idk how ot do it properly
"""

from typing import Any

from reusable_mongodb_connection.get_db import get_db
from reusable_mongodb_connection.exceptions import ReusableMongodbConnectionError

try:
    import fastapi
except ImportError:
    fastapi = None

get_collection = None

if fastapi is not None:
    fastapi: Any

    def get_collection(mongo_url: Any, collection_name: str):
        try:
            db = get_db(mongo_url)
        except ReusableMongodbConnectionError as e:
            print("Connection to DB was unsuccessful")
            print(f"Exception: {e}")
            raise fastapi.HTTPException(status_code=500, detail="Connection to DB was unsuccessful")

        if collection_name not in db.list_collection_names():
            print("Collection not found")
            raise fastapi.HTTPException(
                status_code=500,
                detail="Collection not found",
            )

        return db.facts
