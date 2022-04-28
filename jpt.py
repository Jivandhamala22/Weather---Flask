# import all functions from the tkinter
from tkinter import *
from tkinter import messagebox
import requests, json
from math import *

# function to find weather details
# of any city using openweathermap api
# import required modules

# enter your api key here
api_key = 'fcf5a2b2e92818d83f5196ee2e58770b'

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# take a city name from city_field entry box
city_name = str(input('city name'))

# complete_url variable to store complete url address
complete_url = base_url + 'appid=' + api_key + '&q=' + city_name

# get method of requests module

# return response object
response = requests.get(complete_url)

# json method of response object convert
# json format data into python format data
x = response.json()
print(x['sys']['sunset'])


from datetime import datetime

ts = int(x['sys']['sunset'])

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

coords = {'longitude' : 145, 'latitude' : -38 }


# Sunrise time UTC (decimal, 24 hour format)
print (sun.getSunriseTime( coords )['decimal'])

# Sunset time UTC (decimal, 24 hour format)
print (sun.getSunsetTime( coords )['decimal'])