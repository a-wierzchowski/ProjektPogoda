from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Charts:
    def __init__(self, list_days):
       self.list_days = list_days

    def lineplot_temp(self):
        self.list_days.sort(key=lambda d: d.date)

        # Ekstrahujemy dane
        dates = []
        temps = []

        for day in self.list_days:
            date_obj = datetime.fromtimestamp(day.date)
            dates.append(date_obj)
            temps.append(day.temp)

        # Tworzymy wykres
        plt.figure(figsize=(10, 5))
        plt.plot(dates, temps, marker='o', linestyle='-', color='tab:red')

        plt.title("Temperatura w czasie")
        plt.xlabel("Data")
        plt.ylabel("Temperatura (°C)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def lineplot_humidity(self):
        self.list_days.sort(key=lambda d: d.date)

        # Ekstrahujemy dane
        dates = []
        humidityList = []

        for day in self.list_days:
            date_obj = datetime.fromtimestamp(day.date)
            dates.append(date_obj)
            humidityList.append(day.humidity)

        # Tworzymy wykres
        plt.figure(figsize=(10, 5))
        plt.plot(dates, humidityList, marker='o', linestyle='-', color='tab:red')

        plt.title("Temperatura w czasie")
        plt.xlabel("Data")
        plt.ylabel("Temperatura (°C)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()