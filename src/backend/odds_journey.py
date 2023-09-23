import sqlite3

class Odds():
    def __init__(self, departure, arrival, autonomy, db_manager):
        """
        _summary_

        Args:
            departure (string): Planet of departure
            arrival (string): Panet of arrival
            autonomy (integer): Autonomy in days
            db_manager (Db_manager): DB connector
        """
        self.__departure = departure
        self.__arrival = arrival
        self.__autonomy = autonomy
        self.__db_manager = db_manager

    def start_journey(self, empire_plan):
        """
        Compute odds from a given empire plan

        Args:
            empire_plan (EmpirePlan): Empire plan for this journey
        """
        try:
            routes = self.__db_manager.list_routes()
        except sqlite3.OperationalError as e:
            print(f"Error while getting routes list: {e}")
            raise
    
        print(f"From: {self.__departure}")
        print(f"To: {self.__arrival}")
        print(f"Autonomy: {self.__autonomy}")
        print(f"Coutdown: {empire_plan.get_countdown()}")
        for h in empire_plan.get_bounty_hunters():
            print(f"Hunter: planet = {h.get_planet()}, day = {h.get_day()}")

        paths = self.next_hop(self.__departure, "", self.__arrival, empire_plan.get_countdown(), self.__autonomy, self.__autonomy, routes, 0, [])

        print(paths)

        # Compute new duration from hunters
        for p in paths:
            penalty = self.get_hunters_penalty(p[0])
            p[1]  = penalty * p[1]

    def next_hop(self, current_planet, origin_planet, destination, countdown, autonomy, max_autonomy, routes, duration, ways):
        """ Search for next hop

        Args:
            current_planet (_type_): _description_
            destination (_type_): _description_
            countdown (_type_): _description_
            autonomy (_type_): _description_
            max_autonomy (_type_): _description_
            routes (_type_): _description_
            duration (_type_): _description_
            paths (_type_): _description_
        """
        # Search for next planet hop in available routes
        for r in routes:
            __planets = r[0:2]
            __distance = r[2]

            # If current planet is in the planet couple and origin is not (to avoid backward hop) we try to hop
            try:
                planet_idx = __planets.index(current_planet)

                print(__planets)
                print(planet_idx)
                print( origin_planet not in __planets)
                print(f"origin {origin_planet}")
                print(f"duration {duration}")
                print(f"duration + __distance  {duration + __distance }")
                print(f"countdown  {countdown}")

                if origin_planet not in __planets:
                    # Try to jump only if time allows it
                    if duration + __distance < countdown:
                        # Jump to next planet
                        if __distance < autonomy:
                            autonomy -= __distance
                            duration += __distance

                            # Look for next planet index
                            next_planet_idx = (planet_idx + 1) % 2
                            next_planet = __planets[next_planet_idx]
                            ways.append((next_planet, duration))

                            print(f"autonomy {autonomy}")
                            print(f"duration {duration}")
                            print(f"next_planet {next_planet}")
                            print(f"ways {ways}")
                        # refuel
                        else:
                            next_planet = current_planet
                            duration += 1
                            autonomy = max_autonomy

                        # While destination not reached => next hop
                        if next_planet != destination:
                            for __new_ways in self.next_hop(next_planet, current_planet, destination, countdown, autonomy, max_autonomy, routes, duration, ways):
                                __next_hop_path = __new_ways[0]
                                __next_hop_duration = __new_ways[1]

                                # Concat path to get a complete route
                                if __next_hop_duration <= countdown:
                                    for i in range(len(ways)):
                                        ways[i][0] = ways[i] + __next_hop_path
                                        ways[i][1] = __next_hop_duration
            except ValueError:
                # Planet not in planet couple
                pass

        return ways
        
    def get_hunters_penalty(self, path):
        """ Compute hunter delay

        Args:
            path (Array): List of planet

        Returns
        """
        return 1