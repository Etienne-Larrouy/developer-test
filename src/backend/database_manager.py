class Db_manager():
    def __init__(self, db_url):
        """
        Init db connection

        Args:
            db_url (string): Db path
        """
        self.__db_url = db_url