import os
from datetime import datetime

import requests
import Day


class ConnectAPI:
    def __init__(self):
        self.api_key = os.environ.get("WEATHER_API_KEY")
        if not self.api_key:
            self.api_key = input("Wpisz API key do OpenWeatherMap: ")


    def get_respone(self, city, country):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={self.api_key}&units=metric&lang=pl"
        response  = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            day = Day.Day(
                int(datetime.now().timestamp()),
                data['sys']['country'],
                data['name'],
                data['weather'][0]['description'],
                data['main']['temp'],
                data['main']['humidity'],
                data.get("rain", {}).get("1h", 0.0),
                data['main']['pressure'],
                data['wind']['speed'] * 3.6  # przeliczenie z  m/s na km/h
            )
            return day

        else:
            print("Błąd:", data.get("message", "Nieznany błąd"))
            return None
