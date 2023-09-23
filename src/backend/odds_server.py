import json

from sanic import Sanic
from sanic.response import json as sanicjson
from sanic.exceptions import SanicException

from src.backend.model.empire_plan import EmpirePlan
from src.backend.config import MILLENIUM_CONFIG
from src.backend.odds_journey import Odds
from src.backend.database_manager import Db_manager

app = Sanic("odds")

db_manager = Db_manager(MILLENIUM_CONFIG['routes_db'])
odds = Odds(MILLENIUM_CONFIG['departure'], MILLENIUM_CONFIG['arrival'], MILLENIUM_CONFIG['autonomy'], db_manager)

@app.route('/odds')
async def odds_from_json(request):
    """
    _summary_

    Args:
        request (Request): Request from HTTP

    Returns:
        Json: Odds value
    """
    try:
        empire_plan_json = request.files.get("empire_plan.json").body
        plan = EmpirePlan(**json.loads(empire_plan_json))
        odds_result = odds.start_journey(plan) * 100

        return sanicjson({"odds": odds_result})
    except Exception as e:
        raise SanicException("Something went wrong.", status_code=500) # , quiet=True
        

