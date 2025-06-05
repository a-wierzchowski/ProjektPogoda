import sys
import os
from PyQt5 import QtWidgets, uic
from dotenv import set_key, load_dotenv

from Database import Database
from WeatherAPI import WeatherAPI
from Day import Day

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./assets/MainWindow.ui", self)  # Ładowanie .ui

        # Deklaracje:
        ### Okno API (0)
        self.api_input = self.findChild(QtWidgets.QLineEdit, "api_text")
        self.save_checkbox = self.findChild(QtWidgets.QCheckBox, "checkBox")
        self.group_api = self.findChild(QtWidgets.QGroupBox, "windowAPI")
        self.button_next = self.findChild(QtWidgets.QPushButton, "pushButton")
        ### Okno wyboru miasta (1)
        self.city_input = self.findChild(QtWidgets.QLineEdit, "city_text")
        self.country_input = self.findChild(QtWidgets.QLineEdit, "country_text")
        self.button_find = self.findChild(QtWidgets.QPushButton, "find_Button")
        ### Okno pogody (2)
        self.weather_label = self.findChild(QtWidgets.QLabel, "pogoda_text")
        self.button_change_api = self.findChild(QtWidgets.QPushButton, "change_api_button")
        self.button_change_city = self.findChild(QtWidgets.QPushButton, "change_city_button")
        self.button_refresh = self.findChild(QtWidgets.QPushButton, "refresh_button")

        #Triggery
        self.button_next.clicked.connect(self.window_api_button)
        self.button_find.clicked.connect(self.window_find_button)
        self.button_change_api.clicked.connect(self.window_button_change_api)
        self.button_change_city.clicked.connect(self.window_button_change_city)
        self.button_refresh.clicked.connect(self.window_button_refresh)

        #Setup
        self.database = Database()
        self.weather_api = WeatherAPI()
        if self.weather_api.is_configured():
            self.switch_to_find_window()
        else:
            self.stackedWidget.setCurrentIndex(0)

        self.show()

    #Przycisk w Window API
    def window_api_button(self):

        api_key = self.api_input.text()

        if not api_key:
            QtWidgets.QMessageBox.warning(self, "Błąd", "Wprowadź API key.")
            return

        if not self.weather_api.check_api(api_key):
            QtWidgets.QMessageBox.warning(self, "Błąd", "Wprowadzony API key jest niepoprawny.")
            return
        if self.save_checkbox.isChecked():
            self.weather_api.set_api_key(api_key, True)
        else:
            self.weather_api.set_api_key(api_key, False)

        self.switch_to_find_window()

    def switch_to_find_window(self):
        load_dotenv()
        self.city = os.getenv("CITY")
        self.country = os.getenv("COUNTRY")
        if self.city and self.country:
            weatherNow = self.weather_api.get_respone(self.city, self.country)
            self.switch_to_weather_page(weatherNow)
            return
        self.stackedWidget.setCurrentIndex(1)

    #Przycisk w szukaniu miasta
    def window_find_button(self):
        self.city = self.city_input.text()
        self.country = self.country_input.text()

        set_key(".env", "CITY", self.city)
        set_key(".env", "COUNTRY", self.country)

        weatherNow = self.weather_api.get_respone(self.city, self.country)
        #self.database.add_row_by_day(weatherNow)

        self.switch_to_weather_page(weatherNow)

    def switch_to_weather_page(self, weatherNow):
        self.stackedWidget.setCurrentIndex(2)
        self.weather_label.setText(weatherNow.to_string())

    def window_button_change_api(self):
        self.weather_api.remove_api_key()
        self.stackedWidget.setCurrentIndex(0)

    def window_button_change_city(self):
        self.stackedWidget.setCurrentIndex(1)

    def window_button_refresh(self):
        weatherNow = self.weather_api.get_respone(self.city, self.country)
        self.switch_to_weather_page(weatherNow.to_string())

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()

    sys.exit(app.exec_())