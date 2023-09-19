from sanic import Sanic
from sanic.response import json

from src.backend.model.empire_plan import EmpirePlan
from src.backend.model.scenario import Scenario
from src.backend.config import MILLENIUM_CONFIG
from src.backend.compute_odds import Odds
from src.backend.database_manager import Db_manager

import json
app = Sanic("odds")

odds = Odds(MILLENIUM_CONFIG['departure'], MILLENIUM_CONFIG['arrival'], MILLENIUM_CONFIG['autonomy'])
db_manager = Db_manager(MILLENIUM_CONFIG['departure'])

@app.route('/odds')
async def odds_from_json(request):
    """
    _summary_

    Args:
        request (Request): Request from HTTP

    Returns:
        Json: Odds value
    """
    empire_plan_json = request.files.get("empire_plan.json").body
    odds.start_journey(empire_plan_json)
    return json(empire_plan_json)
