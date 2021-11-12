# reusable_mongodb_connection

This is a repository for reusable component for connecting to MongoDB database with specefied URI and databse (optional)

## Examples:
 1. Get default database by specified URI:
    ```py
    import reusable_mongodb_connection

    URI = "mongodb://localhost/"

    db = reusable_mongodb_connection.get_db(URI)
    ```
 2. Get database by name (if no database with specified database exists, get default database)
     ```py
    from reusable_mongodb_connection import get_db

    URI = "mongodb://localhost/"
    database = "test"

    db = get_db(URI, database)
    ```
 3. Example of real world usage: [corona_travel_server](https://github.com/Corona-Travel/corona-travel_server/blob/dev/src/corona_travel_server/app.py#L31)
 
