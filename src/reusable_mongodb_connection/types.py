"""
types for reusable_mongodb_connection
"""

from pydantic import AnyUrl


class MongoDBURI(AnyUrl):
    """
    as per `https://docs.mongodb.com/manual/reference/connection-string/`

    mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]

    Note
    ----
    might (very likely) not work for clusters, need to redefine host validator
    https://github.com/samuelcolvin/pydantic/blob/master/pydantic/networks.py
    """

    allowed_schemes = {
        "mongodb",
        "mongodb+srv",
    }
