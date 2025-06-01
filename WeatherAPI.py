import os
import requests

class ConnectAPI:
    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")
        if not self.api_key:
            self.api_key = input("Wpisz API key do OpenWeatherMap: ")


    def get_respone(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric&lang=pl"
        response  = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            print(f"Pogoda w {city}: {data['weather'][0]['description']}")
            print(f"Temperatura: {data['main']['temp']}°C")
            print(f"Wilgotność: {data['main']['humidity']}%")
        else:
            print("Błąd:", data.get("message", "Nieznany błąd"))
