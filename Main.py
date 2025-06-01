import  WeatherAPI
conn = WeatherAPI.ConnectAPI()

today = conn.get_respone("Brodnica", "PL")

today.print()