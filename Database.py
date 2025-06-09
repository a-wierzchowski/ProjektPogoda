import os
import sqlite3
from datetime import datetime, timedelta
from typing import List

from Day import Day

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

        dt = datetime.fromtimestamp(date)
        start_of_day = datetime(dt.year, dt.month, dt.day)
        end_of_day = start_of_day + timedelta(days=1)

        start_date = int(start_of_day.timestamp())
        end_date = int(end_of_day.timestamp())

        self.cursor.execute("SELECT date FROM history_weather WHERE date >= ? AND date <= ? AND country = ? AND city = ?", (start_date, end_date, country, city))
        rows = self.cursor.fetchall()

        if not rows:
            self.cursor.execute(f"INSERT INTO history_weather VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (date, country, city, description, temp, humidity, rain, pressure, wind))
            self.conn.commit()

    #def read_by_day(self, start_day, start_month, start_year, end_day, end_month, end_year, city) -> List[Day]:
    def read_by_day(self, date, city, country) -> List[Day]:

        #start_date = int( datetime(start_year, start_month, start_day).timestamp() )
        #end_date = int( datetime(end_year, end_month, end_day).timestamp() )

        dt = datetime.fromtimestamp(date)
        start_of_day = datetime(dt.year, dt.month, dt.day+1)
        end_of_day = start_of_day - timedelta(days=7)

        start_date = int(start_of_day.timestamp())
        end_date = int(end_of_day.timestamp())

        self.cursor.execute("SELECT * FROM history_weather WHERE date >= ? AND date <= ? AND city = ? AND country = ?", (end_date, start_date, city, country))
        rows = self.cursor.fetchall()

        days_list = []

        for row in rows:
            day = Day(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            days_list.append(day)

        return days_list