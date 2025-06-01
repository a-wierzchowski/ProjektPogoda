from Database import Database
from WeatherAPI import WeatherAPI
from Charts import Charts
from Day import Day
from Interface import Interface

connAPI = WeatherAPI()
database = Database()
interface = Interface()

def main():



    weatherNow = (Day)
    #weatherNow = connAPI.get_respone("Brodnica", "PL")
    #weatherNow.print()
    #database.add_row_by_day(weatherNow)
    # database.add_row(weatherNow.date, weatherNow.country, weatherNow.city, weatherNow.description, weatherNow.temp, weatherNow.humidity, weatherNow.rain, weatherNow.pressure, weatherNow.wind)

    #list_days = database.read_by_day(1,5,2025,2,6,2025)
    #charts = Charts(list_days)
    #charts.lineplot_temp()
    # list_days[0].print()



if __name__ == "__main__":
    main()