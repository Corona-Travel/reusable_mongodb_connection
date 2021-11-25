class ReusableMongodbConnectionError(ValueError):
    def __init__(self, description: str = "An error occurred in reusable_mongodb_connection", *args, **kwargs):
        super().__init__(description, *args, **kwargs)
