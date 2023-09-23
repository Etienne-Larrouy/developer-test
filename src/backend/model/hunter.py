

class Hunter():
    def __init__(self, planet, day):
        """
        Args:
            planet (Hunters): Planet of stay
            day (integer): Day number
        """
        self.__planet = planet
        self.__day = day

    def get_planet(self):
        """ Planet name getter

        Returns:
            String: Planet name
        """
        return self.__planet

    def get_day(self):
        """
        Day number getter
        Returns:
            Integer: Day number
        """
        return self.__day