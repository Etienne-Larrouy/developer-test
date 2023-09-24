import sqlite3
import os
from utils.logger import Logger

# instance of logger class
logger = Logger.get_instance()

class Db_manager():
    def __init__(self, *db_url):
        """
        Init db connection

        Args:
            db_url (string): Db path
        """
        opened = False

        # Test all url given as param
        for url in db_url:
            logger.get_logger().info(f"url: {url}")
            if os.path.exists(url):
                self.__con = sqlite3.connect(url)
                logger.get_logger().info(f"Database succesfully opened.")
                opened = True
                break

        # Raise exception if no url worked
        if not opened:
            raise Exception("Database doesn't exist.")

    def list_routes(self):
        """
        Return list of routes
        """
        cur = self.__con.cursor()
        res = cur.execute("SELECT * FROM ROUTES;")
        
        return res.fetchall()
