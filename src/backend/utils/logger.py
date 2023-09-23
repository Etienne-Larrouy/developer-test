import logging
from logging.handlers import TimedRotatingFileHandler

class Logger:
    """ 
        Class used to log pushed values and applications log
    """

    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """

        if Logger.__instance is None:
            Logger()	
        return Logger.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if Logger.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            # Init logger files
            Logger.__instance = self

            # Init rotating log            
            self.logger = logging.getLogger("Rotating Log")
            self.logger.setLevel(logging.INFO)
            formatter = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")            
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(console_handler)

    # Return logger
    def get_logger(self):
        """
        Logger object
        """
        return self.logger
