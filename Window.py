import sys
import os
from PyQt5 import QtWidgets, uic
from Database import Database
from WeatherAPI import WeatherAPI
from Day import Day

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./assets/MainWindow.ui", self)  # Ładowanie .ui

        # Deklaracje:
        ### Okno API
        self.api_input = self.findChild(QtWidgets.QLineEdit, "api_text")
        self.save_checkbox = self.findChild(QtWidgets.QCheckBox, "checkBox")
        self.group_api = self.findChild(QtWidgets.QGroupBox, "windowAPI")
        self.button_next = self.findChild(QtWidgets.QPushButton, "pushButton")
        ### Okno wyboru miasta
        self.city_input = self.findChild(QtWidgets.QLineEdit, "city_text")
        self.country_input = self.findChild(QtWidgets.QLineEdit, "country_text")
        self.button_find = self.findChild(QtWidgets.QPushButton, "findButton")

        #Triggery
        self.button_next.clicked.connect(self.window_api_button)
        self.button_find.clicked.connect(self.window_find_button)

        #Setup
        self.database = Database()
        self.weather_api = WeatherAPI()
        if self.weather_api.is_configured():
            self.windowAPI.setVisible(False)
            self.windowCitySelect.setVisible(True)
        else:
            self.windowAPI.setVisible(True)
            self.windowCitySelect.setVisible(False)

        self.show()

    #
    def window_api_button(self):

        api_key = self.api_input.text()

        if not api_key:
            QtWidgets.QMessageBox.warning(self, "Błąd", "Wprowadź API key.")
            return

        if not self.weather_api.check_api(api_key):
            QtWidgets.QMessageBox.warning(self, "Błąd", "Wprowadzony API key jest niepoprawny.")
            return
        if self.save_checkbox.isChecked():
            self.weather_api.set_api_key(api_key)
        self.windowAPI.setVisible(False)
        self.windowCitySelect.setVisible(True)

    def window_find_button(self):
        city = self.city_input.text()
        country = self.country_input.text()

        weatherNow = self.weather_api.get_respone(city, country)
        weatherNow.print()
        self.database.add_row_by_day(weatherNow)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()

    sys.exit(app.exec_())