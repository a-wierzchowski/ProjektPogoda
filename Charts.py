from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Charts:
    def __init__(self, list_days):
       self.list_days = sorted(list_days, key=lambda d: d.date)

    def draw_temperature_chart(self, canvas):
        dates = []
        temps = []

        dni_tygodnia = {
            'Monday': 'Pon',
            'Tuesday': 'Wt',
            'Wednesday': 'Śr',
            'Thursday': 'Czw',
            'Friday': 'Pi',
            'Saturday': 'Sob',
            'Sunday': 'Nied'
        }

        for day in self.list_days:
            english_day = datetime.fromtimestamp(day.date).strftime('%A')
            date_obj = dni_tygodnia[english_day]
            dates.append(date_obj)
            temps.append(day.temp)

        ax = canvas.axes
        ax.clear()
        ax.plot(dates, temps, marker='o', color='tab:red')
        ax.set_title("Temperatura z ostatnich zapisanych 7 dni")
        ax.set_xlabel("Data")
        ax.set_ylabel("Temp (°C)")
        ax.grid(True)
        canvas.draw()

    def lineplot_temp(self):

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