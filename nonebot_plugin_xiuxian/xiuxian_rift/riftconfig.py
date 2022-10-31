import json
import os
from pathlib import Path

configkey = []
CONFIG = {
    "rank": {
        "黄级秘境": {
            "type_rate": 200,
            "rank":2
        },
        "人级秘境": {
            "type_rate": 50,
            "rank":4
        },
        "地级秘境": {
            "type_rate": 25,
            "rank":6
        }, 
        "天级秘境": {
            "type_rate": 12,
            "rank":8
        },
        "仙级秘境": {
            "type_rate": 6,
            "rank":10
        }
    }
}

def get_config():
    try:
        config = readf()
        for key in configkey:
            if key not in list(config.keys()):
                config[key] = CONFIG[key]
        savef(config)
    except:
        config = CONFIG
        savef(config)
    return config

CONFIGJSONPATH = Path(__file__).parent
FILEPATH = CONFIGJSONPATH / 'config.json'
def readf():
    with open(FILEPATH, "r", encoding="UTF-8") as f:
        data = f.read()
    return json.loads(data)


def savef(data):
    data = json.dumps(data, ensure_ascii=False, indent=3)
    savemode = "w" if os.path.exists(FILEPATH) else "x"
    with open(FILEPATH, mode=savemode, encoding="UTF-8") as f:
        f.write(data)
        f.close
    return True
