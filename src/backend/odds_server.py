import json

from sanic import Sanic
from sanic.response import json as sanicjson
from sanic.exceptions import SanicException

from model.empire_plan import EmpirePlan
from sanic_cors import CORS
from config import MILLENIUM_CONFIG
from odds_journey import Odds
from database_manager import Db_manager

app = Sanic(__name__)
CORS(app, automatic_options=True)

db_manager = Db_manager(MILLENIUM_CONFIG['routes_db'])
odds = Odds(MILLENIUM_CONFIG['departure'], MILLENIUM_CONFIG['arrival'], MILLENIUM_CONFIG['autonomy'], db_manager)

@app.route('/odds', methods=['POST', 'OPTIONS'])
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
        

if __name__ == "__main__":
    app.run(port=8080)