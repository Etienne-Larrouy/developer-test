import json
import os
from pathlib import Path
import pytest

from src.backend.model.empire_plan import EmpirePlan
from src.backend.model.scenario import Scenario
from src.backend.config import MILLENIUM_CONFIG
from src.backend.odds_journey import Odds
from src.backend.database_manager import Db_manager

def test_example_1():
    with open("src/backend/tests/examples/example1/millennium-falcon.json") as millenium_file:
        MILLENIUM_CONFIG = json.load(millenium_file)

    with open("src/backend/tests/examples/example1/empire.json") as empire_plan_json:
        plan = EmpirePlan(**json.load(empire_plan_json))

    db_manager = Db_manager("src/backend/tests/examples/example1/" + MILLENIUM_CONFIG['routes_db'])
    odds = Odds(MILLENIUM_CONFIG['departure'], MILLENIUM_CONFIG['arrival'], MILLENIUM_CONFIG['autonomy'], db_manager)
        
    odds.start_journey(plan)

    assert odds == b"foo"
    