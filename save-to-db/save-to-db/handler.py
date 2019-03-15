from pymongo import MongoClient
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    secret = ''
    with open ('/var/openfaas/secrets/secret-api-key') as fin:
        for line in fin:
            secret = line
            break


    client = MongoClient('mongodb://main_admin:{0}@mongodb-service.default.svc/mysinoptik'.format(secret), 27017)

    db = client.mysinoptik
    collection_weth = db.weather
    collection_seis = db.seismicity
    json_text = json.loads(req)

    key = json_text["type"]

    if key == 'weather':
        del json_text["type"]
        collection_weth.save(json_text)
    else:
        del json_text["type"]
        collection_seis.save(json_text)
