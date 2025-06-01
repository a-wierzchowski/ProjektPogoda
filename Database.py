import os
import sqlite3

import requests
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("history_weather.db")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def add_row_by_day(self, day):
        self.add_row(day.date, day.country, day.city, day.description, day.temp, day.humidity, day.rain, day.pressure, day.wind)

    def add_row(self, date, country, city, description, temp, humidity, rain, pressure, wind):
        self.cursor.execute(f"SELECT date FROM history_weather where date = {date}")
        rows = self.cursor.fetchall()

        if not rows:
            self.cursor.execute(f"INSERT INTO history_weather VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (date, country, city, description, temp, humidity, rain, pressure, wind))
            self.conn.commit()

    def read_by_day(self, date):
        self.cursor.execute("SELECT * FROM history_weather")
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)
