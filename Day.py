import os
from datetime import datetime

import requests
class Day:
    def __init__(self, date, country, city, description, temp, humidity, rain, pressure, wind):
        self.date = date
        self.country = country
        self.city = city
        self.description = description
        self.temp = temp
        self.humidity = humidity
        self.rain = rain
        self.pressure = pressure
        self.wind = round(wind * 3.6, 2) # przeliczenie z  m/s na km/h

    def print(self):
        print(f"Data:\t\t {datetime.fromtimestamp(self.date)}")
        print(f"Miejsce:\t {self.country} {self.city}")
        print(f"Niebo:\t\t {self.description}")
        print(f"Temperatura: {self.temp}°C")
        print(f"Wilgotność:\t {self.humidity} %")
        print(f"Deszcz:\t\t {self.rain} mm")
        print(f"Ciśnienie:\t {self.pressure} hPa ")
        print(f"Wiatr:\t\t {self.wind} km/h")
