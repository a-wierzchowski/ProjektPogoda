import sys
from Database import Database
from WeatherAPI import WeatherAPI
from Day import Day
from Window import MyApp
from PyQt5 import QtWidgets


def setup(connAPI, window):
    None
    #Parametry startowe
    #weatherNow = (Day)
    #weatherNow = weather_api.get_respone("Torun", "PL")
    #weatherNow.print()



    # Testy
    #database.add_row_by_day(weatherNow)
    #database.add_row(weatherNow.date, weatherNow.country, weatherNow.city, weatherNow.description, weatherNow.temp, weatherNow.humidity, weatherNow.rain, weatherNow.pressure, weatherNow.wind)

    #list_days = database.read_by_day(1,5,2025,2,6,2025, "Torun")
    #charts = Charts(list_days)
    #charts.lineplot_temp()
    # list_days[0].print()



