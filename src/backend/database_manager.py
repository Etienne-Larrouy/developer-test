import sqlite3
import os

class Db_manager():
    def __init__(self, db_url):
        """
        Init db connection

        Args:
            db_url (string): Db path
        """
        if os.path.exists(db_url):
            self.__con = sqlite3.connect(db_url)
        else:
            raise Exception("Database doesn't exist.")

    def list_routes(self):
        """
        Return list of routes
        """
        cur = self.__con.cursor()
        res = cur.execute("SELECT * FROM ROUTES;")
        
        return res.fetchall()
