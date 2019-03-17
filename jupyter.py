import requests
import json
import ipywidgets as widgets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

from IPython.display import clear_output

%matplotlib inline

button = widgets.Button(description="Draw graph")
display(button)
out = widgets.Output()
city = widgets.Dropdown(
    options=['Kyiv', 'Lviv', 'Odessa'],
    value='Odessa',
    description='Cities:',
    disabled=False,
)

type_data = widgets.Dropdown(
    options=['temp', 'hum', 'v_wind', 'mag', 'depth'],
    value='temp',
    description='Available data:',
    disabled=False,
)

min_max_value = widgets.FloatRangeSlider(
    value=[0, 15],
    min=-100.0,
    max=100.0,
    step=0.1,
    description='Value:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

date_from = widgets.Text(
    value='2019-03-10 22:58:54',
    placeholder='Type something',
    description='Date from:',
    disabled=False
)

date_to = widgets.Text(
    value='2019-03-15 22:58:54',
    placeholder='Type something',
    description='Date to:',
    disabled=False
)


display(city, type_data, min_max_value, date_from, date_to)

def click_button(b):
    arg = {"city": city.value, "data": type_data.value,
           "val_min": min_max_value.value[0],
           "val_max": min_max_value.value[1],
           "time_min": date_from.value,
           "time_max": date_to.value}
    r = requests.post('http://gateway.openfaas.svc:8080/function/get-from-db', json.dumps(arg))
    my_plot = r.content.plot(kind='bar')
    with out:
        clear_output()
        
button.on_click(click_button)