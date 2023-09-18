from sanic import Sanic
from sanic.response import json

from src.backend.model.empire_plan import EmpirePlan
from src.backend.model.scnario import Scenario
from src.backend.compute_odds import Odds
import json

app = Sanic("odds")

milennium_config = 
odds = Odds(milennium_config)

@app.route('/odds')
async def odds_from_json(request):
    empire_plan_json = rrequest.files.get("empire_plan.json").body
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run()