class Odds():
    def __init__(self, departure, arrival, autonomy):
        """
        _summary_

        Args:
            departure (string): Planet of departure
            arrival (string): Panet of arrival
            autonomy (integer): Autonomy in days
        """
        self.__departure = departure
        self.__arrival = arrival
        self.__autonomy = autonomy

    def start_journey(self, empire_plan):
        """
        Compute odds from a given empire plan

        Args:
            empire_plan (EmpirePlam): Empire plan for this journey
        """
        print(empire_plan)