import json
from weatherKey import *
import requests
import datetime
import time
import matplotlib.pyplot as plt

# current_weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}'.format('tampa', weatherKey))
# print(json.dumps(current_weather.json(), indent=4))

forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={0}&mode=json&APPID={1}'.format('tampa', weatherKey))
# print(forecast.json())
# print(json.dumps(forecast.json(), indent=4))
lst = forecast.json()['list']


def get_data(lst):
    timestamps = []
    times = []
    temps = []
    for entry in lst:
        timestamp = entry['dt']
        timestamps.append(timestamp)
        value = datetime.datetime.fromtimestamp(timestamp)
        times.append(value.strftime('%m/%d/%y %-I:%M %p'))

        temp = entry['main']['temp']
        temp_f = round((9/5)*(temp - 273) + 32, 1)
        temps.append(temp_f)
    data = {
        'timestamps': timestamps,
        'times': times,
        'temps': temps
    }
    return data


data = get_data(lst)
print(data)

plt.plot(data['timestamps'], data['temps'])
# plt.xticks(data['timestamps'], data['times'])
plt.show()
