from src.backend.model.hop import Hop

class Path():
    def __init__(self, planet, duration, autonomy):
        self.__hops = []
        self.add_hop(planet, 0)
        self.__duration = duration
        self.__autonomy = autonomy

    def already_went_here(self, planet):
        """ Check if planet is in path already

        Args:
            planet (str): Planet

        Returns:
            str: planet
        """
        exists = False
        for h in  self.__hops:
            if planet == h.get_planet():
                exists = True
        return exists

    def get_current_planet(self):
        """ Return current planet

        Returns:
            str: planet
        """
        return self.__hops[-1].get_planet()

    def add_hop(self, planet, day):
        """ add planet to path

        Args:
            planet (str): Planet
        """
        h = Hop(planet, day)
        self.__hops.append(h)

    def get_hops(self):
        """ Get path

        Returns:
            Array: List of hop
        """
        return self.__hops

    def set_autonomy(self, autonomy):
        """ set new autonomy

        Args:
            autonomy (integer): New autonomy
        """
        self.__autonomy = autonomy

    def get_autonomy(self):
        """ Get autonomy
        Returns:
            integer: autonomy
        """
        return self.__autonomy

    def remove_autonomy(self, days):
        """ Remove days to autonomy
        Args:
            days (integer): days
        """
        self.__autonomy -= days
    
    def add_autonomy(self, days):
        """ Add days to autonomy
        Args:
            days (integer): days
        """
        self.__autonomy += days

    def get_duration(self):
        """ Get path duration
        Returns:
            integer: duration
        """
        return self.__duration

    def add_duration(self, days):
        """ Add days to duration
        Args:
            days (integer): days
        """
        self.__duration += days


