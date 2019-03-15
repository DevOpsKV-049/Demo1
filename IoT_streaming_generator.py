import json
import requests
from random import randint, uniform
from datetime import datetime
import time
import os


list_of_city = ['Kyiv', 'Lviv', 'Odessa']


def iot_streaming_data():  # generate streaming random data as IoT devices
    while True:
        data = {'type': 'weather',
                'city': list_of_city[randint(0, len(list_of_city) - 1)],
                'temp': randint(-40, 100),
                'v_wind': round(uniform(0, 60), 1),
                'hum': randint(0, 100),
                'time': str(datetime.now())}

        # connect with env and send data to async-function stream-mod
        r = requests.post(os.environ['FAAS'] + '/async-function/stream-mod', json.dumps(data))
        print(r.status_code, "Data sent!")
        time.sleep(1)


iot_streaming_data()

