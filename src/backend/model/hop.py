class Hop():
    def __init__(self, __planet, __day):
        """ Defines a hop

        Args:
            __planet (str): Planet
            __day (integer): Day of stay
        """
        self.planet = __planet
        self.day = __day

    def get_planet(self):
        """ Get planet

        Returns:
            str: planet
        """
        return self.planet

    def get_day(self):
        """ Get day
        Returns:
            integer: day
        """
        return self.day