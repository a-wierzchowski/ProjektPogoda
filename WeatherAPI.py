import os
from datetime import datetime
from dotenv import load_dotenv

import requests
from Day import Day


class WeatherAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("WEATHER_API_KEY")

    def set_api_key(self, api_key):
        with open(".env", "w") as f:
            f.write(f"WEATHER_API_KEY={api_key}\n")

    def check_api(delf, api_key):
        url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            return True

        return False

    def is_configured(self):
        return bool(self.api_key)



    def get_respone(self, city, country) -> Day | None:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={self.api_key}&units=metric&lang=pl"
        response  = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            day = Day(
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