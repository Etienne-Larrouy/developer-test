import sqlite3
import copy
from model.path import Path
from utils.logger import Logger

# instance of logger class
logger = Logger.get_instance()

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
            logger.get_logger().error(f"Error while getting routes list: {e}")
            raise
    
        logger.get_logger().info(f"From: {self.__departure}")
        logger.get_logger().info(f"To: {self.__arrival}")
        logger.get_logger().info(f"Autonomy: {self.__autonomy}")
        logger.get_logger().info(f"Coutdown: {empire_plan.get_countdown()}")

        for h in empire_plan.get_bounty_hunters():
            logger.get_logger().info(f"Hunter: planet = {h.get_planet()}, day = {h.get_day()}")

        paths = self.get_paths(self.__departure, self.__arrival, empire_plan.get_countdown(), self.__autonomy, routes, empire_plan.get_bounty_hunters())

        best_odds = 0

        # Compute new duration from hunters
        for p in paths:
            penalty = self.get_hunters_penalty(p, empire_plan.get_bounty_hunters())

            new_odds = 1 - penalty

            # Keep only best odds
            if new_odds > best_odds:
                best_odds = new_odds
        
        logger.get_logger().info(f"Odds: {best_odds}")
       
        return best_odds

    def get_paths(self, departure, arrival, countdown, max_autonomy, routes, hunters):
        """ Loof for path from departure to destination following routes

        Args:
            departure (str): Departure planet
            arrival (str): Arrival planet
            countdown (integer): Countdown before end
            max_autonomy (integer): Millenium autonomy in days
            routes (Array): List of routes
            hunters (Array): List of hunters

        Returns:
            Array: List of possible paths
        """
        
        start_route = Path(departure, 0, max_autonomy)
        possible_hops = [start_route]
        next_possible_hops = []
        new_hop = True

        # While a hop is done we continue to search
        while new_hop:
            
            new_hop = False

            # Look for hops for all avilable routes
            for hop in possible_hops:
                if arrival != hop.get_current_planet():
                    for r in routes:
                        planets = r[0:2]
                        distance = r[2]

                        try:
                            # Get next planet name
                            planet_idx = planets.index(hop.get_current_planet())
                            next_planet_idx = (planet_idx + 1) % 2
                            next_planet = planets[next_planet_idx]

                            # Avoid path loop
                            if not hop.already_went_here(next_planet):
                                new_hop = True

                                # Try to jump only if time allows it
                                if hop.get_duration() + distance <= countdown:
                                    jumped = False

                                    # Jump to next planet
                                    if distance <= hop.get_autonomy():
                                        jumped = True
                                        
                                        # Update hop
                                        new_hop = copy.deepcopy(hop)
                                        new_hop.remove_autonomy(distance)
                                        new_hop.add_duration(distance)
                                        new_hop.add_hop(next_planet, new_hop.get_duration())

                                        next_possible_hops.append(new_hop)
                                    
                                    elif hop.get_duration() + distance + 1 <= countdown:
                                        jumped = True
                                        # refuel before jumping then jumps
                                        new_hop = copy.deepcopy(hop)
                                        new_hop.add_hop(hop.get_current_planet(), new_hop.get_duration() + 1)
                                        new_hop.add_duration(distance + 1)
                                        new_hop.add_hop(next_planet, new_hop.get_duration())
                                        new_hop.set_autonomy(max_autonomy)

                                        next_possible_hops.append(new_hop)

                                    if jumped:
                        
                                        # Check if we can wait one more day before jumping if there are hunters on next planet
                                        if self.hunters_on_next_planet(hunters, next_planet, new_hop.get_duration()) and hop.get_duration() + distance + 1 <= countdown:
                                            while (countdown - (hop.get_duration() + distance) - 1) > 0:
                                                # Wait one more day before jumping
                                                new_hop = copy.deepcopy(hop)
                                                new_hop.add_duration(1)
                                                new_hop.add_hop(hop.get_current_planet(), new_hop.get_duration())
                                                new_hop.set_autonomy(max_autonomy)

                                                hop = copy.deepcopy(new_hop)

                                                # Jump to next planet
                                                new_hop.add_duration(distance)
                                                new_hop.add_hop(next_planet, new_hop.get_duration())
                                                new_hop.remove_autonomy(distance)

                                                next_possible_hops.append(new_hop)


                        except ValueError:
                            # Planet not in planet couple
                            pass
                else:
                    next_possible_hops.append(copy.deepcopy(hop))
    
            possible_hops = next_possible_hops
            next_possible_hops = []

        return possible_hops
    
    def hunters_on_next_planet(self, hunters, planet, day):
        """ True if hunters on next planet
        Args:
            hunters (Array): List of hunters
            planet (Str): Next planet
            day (Integer): Day
        """
        hunters_here = False

        for h in hunters:
            if h.get_planet() == planet and h.get_day() == day:
                hunters_here = True
        
        return hunters_here

    def get_hunters_penalty(self, path, hunters):
        """ Compute hunter delay

        Args:
            path (Array): List of planet
            hunters (Array): List of hunters

        Returns
        """
        penalty = 0
        caught = 0
        for h in path.get_hops():
            for hunt in hunters:
                # Same day same planet -> we can by caught by hunters
                if h.get_planet() == hunt.get_planet() and h.get_day() == hunt.get_day():

                    # Compute penalty
                    if caught == 0:
                        penalty = 0.1
                    else:
                        penalty += pow(9, caught) / pow(10, caught + 1)
                    
                    caught +=1

        return penalty