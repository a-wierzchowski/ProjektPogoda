from Database import Database
from WeatherAPI import WeatherAPI



def main():
    connAPI = WeatherAPI()
    database = Database()

    weatherNow = connAPI.get_respone("Brodnica", "PL")
    weatherNow.print()
    #database.add_row_by_day(weatherNow)
    database.add_row(weatherNow.date, weatherNow.country, weatherNow.city, weatherNow.description, weatherNow.temp, weatherNow.humidity, weatherNow.rain, weatherNow.pressure, weatherNow.wind)



if __name__ == "__main__":
    main()