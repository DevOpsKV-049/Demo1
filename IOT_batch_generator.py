import json
import requests
from random import randint, uniform
from datetime import datetime
import time
import os


list_of_city = ['Kyiv', 'Lviv', 'Odessa']


def iot_batch_data():  # generating and sending batch data to modification function in OpenFaaS
    while True:
        batch_data = []
        count_of_timeuot = 0
        while count_of_timeuot < 300:  # append data to batch
            count_of_timeuot += 1
            data = {'type': 'seis_activity',
                    'city': list_of_city[randint(0, len(list_of_city) - 1)],
                    'mag': round(uniform(0, 10)),
                    'depth': randint(0, 500),
                    'time': str(datetime.now())}

            batch_data.append(data)
            time.sleep(1)
        # sending batch data to modification function in OpenFaaS
        r = requests.post(os.environ['FAAS'] + '/async-function/batch-mod', json.dumps(batch_data))

        print(r.status_code, "Data sent!")


iot_batch_data()
