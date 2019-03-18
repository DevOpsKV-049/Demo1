import pymongo
import json
import datetime
#request structure which comes from jupyter notebook
#arg = json.dumps({'city':'Kyiv', 'data': 'hum', 'val_min': 10, 'val_max': 90,
#       'time_min': '2019-03-16 11:16:12', 'time_max': '2019-03-16 17:30:12'})

def handle(req):

#code connects to mongodb
    secret = ''
    with open('/var/openfaas/secrets/secret-api-key') as fin:
        for line in fin:
            secret = line
            break

    client_conn = pymongo.MongoClient('mongodb://main_admin:{0}@mongodb-service.default.svc/mysinoptik'.format(secret), 27017)

    db = client_conn["mysinoptik"]
    coll_1 = db["weather"]
    coll_2 = db["seismicity"]

#parsing request from jupyter notebook and querying data from Mongodb
    arg = json.loads(req)

    if arg['data'] in ["temp", "hum", "v_wind"]:
        array_unprepared = list(coll_1.find({'city': arg['city'], "$and": [{arg["data"]: {"$gte": arg["val_min"]}}, {arg["data"]: {"$lte": arg["val_max"]}}]},
                                            {"_id": 0, arg["data"]: 1, 'time': 1}))
    else:
        array_unprepared = list(coll_2.find({'city': arg['city'], "$and": [{arg["data"]: {"$gte": arg["val_min"]}},
                                                                           {arg["data"]: {"$lte": arg["val_max"]}}]},
                                            {"_id": 0, arg["data"]: 1, 'time': 1}))

    new_array = []
    #here you can see piece of code, which compare dates from mongo with date arg's from notebook.
    #It's happen due to storing dates as strings in mongodb
    for arr_elem in array_unprepared:
        if datetime.datetime.strptime(arg["time_min"], '%Y-%m-%d %X') < datetime.datetime.strptime(arr_elem['time'][0:19], '%Y-%m-%d %X') < datetime.datetime.strptime(arg["time_max"], '%Y-%m-%d %X'):
            new_array.append(arr_elem)

    return json.dumps(new_array)
