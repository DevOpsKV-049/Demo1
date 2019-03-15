import requests
import json


def handle(json_data):
    mod_data_batch = json.loads(json_data)

    for mod_data in mod_data_batch:  # modification data from batch
        mod_data['depth'] = round(mod_data['depth'] * 1.61, 2)

        # sending data to saving function
        requests.post('http://gateway.openfaas.svc:8080/async-function/save-to-db', json.dumps(mod_data))

