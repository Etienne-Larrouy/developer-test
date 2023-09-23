import sqlite3
import os
from utils.logger import Logger

# instance of logger class
logger = Logger.get_instance()

class Db_manager():
    def __init__(self, db_url):
        """
        Init db connection

        Args:
            db_url (string): Db path
        """
        if os.path.exists(db_url):
            self.__con = sqlite3.connect(db_url)
            logger.get_logger().info(f"Database succesfully opened.")
        else:
            raise Exception("Database doesn't exist.")

    def list_routes(self):
        """
        Return list of routes
        """
        cur = self.__con.cursor()
        res = cur.execute("SELECT * FROM ROUTES;")
        
        return res.fetchall()
