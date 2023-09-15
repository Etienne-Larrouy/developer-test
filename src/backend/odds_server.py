from sanic import Sanic
from sanic.response import json

app = Sanic("odds")
app.ctx.db = Database()

@app.route('/api/')
async def odds_from_json(request):
    json = request.file
    return json({'hello': 'world'})

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run()