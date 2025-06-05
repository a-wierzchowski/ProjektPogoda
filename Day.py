from datetime import datetime

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

    def to_string(self) -> str:
        return (f"Data:\t\t {datetime.fromtimestamp(self.date)}\n"
                f"Miejsce:\t\t {self.country} {self.city}\n"
                f"Niebo:\t\t {self.description}\n"
                f"Temperatura:\t {self.temp}°C\n"
                f"Wilgotność:\t {self.humidity} %\n"
                f"Deszcz:\t\t {self.rain} mm\n"
                f"Ciśnienie:\t\t {self.pressure} hPa\n"
                f"Wiatr:\t\t {self.wind} km/h")
