import requests
import json


def handle(json_data):
    mod_data = json.loads(json_data)

    mod_data['temp'] = round((5 / 9) * (mod_data['temp'] - 32), 2)
    mod_data['v_wind'] = round(mod_data['v_wind'] * 1.61, 2)

    r = requests.post('http://gateway.openfaas.svc:8080/async-function/save-to-db', json.dumps(mod_data))

    return r.status_code