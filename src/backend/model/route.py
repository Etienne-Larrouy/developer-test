class Route():
    def __init__(self, origin, destination, travel_time):
        """
        _summary_

        Args:
            origin (string): Origin planet for this route
            destination (string): Destination planet for this route
            travel_time (integer):Travel time in days between <origin> and <destination>
        """
        self.__origin = origin
        self.__destination = destination
        self.__travel_time = travel_time