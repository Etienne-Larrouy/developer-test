import json
import os
from pathlib import Path
import pytest

from model.empire_plan import EmpirePlan
from config import MILLENIUM_CONFIG
from odds_journey import Odds
from database_manager import Db_manager

def test_example_1():
    with open("tests/examples/example1/millennium-falcon.json") as millenium_file:
        MILLENIUM_CONFIG = json.load(millenium_file)

    with open("tests/examples/example1/empire.json") as empire_plan_json:
        plan = EmpirePlan(**json.load(empire_plan_json))

    db_manager = Db_manager("tests/examples/example1/" + MILLENIUM_CONFIG['routes_db'])
    odds = Odds(MILLENIUM_CONFIG['departure'], MILLENIUM_CONFIG['arrival'], MILLENIUM_CONFIG['autonomy'], db_manager)
        
    res = odds.start_journey(plan)

    assert res == 0

def test_example_2():
    with open("tests/examples/example2/millennium-falcon.json") as millenium_file:
        MILLENIUM_CONFIG = json.load(millenium_file)

    with open("tests/examples/example2/empire.json") as empire_plan_json:
        plan = EmpirePlan(**json.load(empire_plan_json))

    db_manager = Db_manager("tests/examples/example2/" + MILLENIUM_CONFIG['routes_db'])
    odds = Odds(MILLENIUM_CONFIG['departure'], MILLENIUM_CONFIG['arrival'], MILLENIUM_CONFIG['autonomy'], db_manager)
        
    res = odds.start_journey(plan)

    assert res == 0.81

def test_example_3():
    with open("tests/examples/example3/millennium-falcon.json") as millenium_file:
        MILLENIUM_CONFIG = json.load(millenium_file)

    with open("tests/examples/example3/empire.json") as empire_plan_json:
        plan = EmpirePlan(**json.load(empire_plan_json))

    db_manager = Db_manager("tests/examples/example3/" + MILLENIUM_CONFIG['routes_db'])
    odds = Odds(MILLENIUM_CONFIG['departure'], MILLENIUM_CONFIG['arrival'], MILLENIUM_CONFIG['autonomy'], db_manager)
        
    res = odds.start_journey(plan)

    assert res == 0.90
    
def test_example_4():
    with open("tests/examples/example4/millennium-falcon.json") as millenium_file:
        MILLENIUM_CONFIG = json.load(millenium_file)

    with open("tests/examples/example4/empire.json") as empire_plan_json:
        plan = EmpirePlan(**json.load(empire_plan_json))

    db_manager = Db_manager("tests/examples/example4/" + MILLENIUM_CONFIG['routes_db'])
    odds = Odds(MILLENIUM_CONFIG['departure'], MILLENIUM_CONFIG['arrival'], MILLENIUM_CONFIG['autonomy'], db_manager)
        
    res = odds.start_journey(plan)

    assert res == 1