
import json

"""
Read config from millennium-falcon.json
"""
MILLENIUM_CONFIG = None

with open("src/backend/config/millennium-falcon.json") as millenium_file:
    MILLENIUM_CONFIG = json.load(millenium_file)