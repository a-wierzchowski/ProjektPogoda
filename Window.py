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

        self.database = Database()
        self.weather_api = WeatherAPI()

        self.api_input = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.save_checkbox = self.findChild(QtWidgets.QCheckBox, "checkBox")
        self.button_next = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.group_api = self.findChild(QtWidgets.QGroupBox, "windowAPI")

        self.button_next.clicked.connect(self.window_api_button)

        if self.weather_api.is_configured():
            self.windowAPI.setVisible(False)
            self.windowCitySelect.setVisible(True)
        else:
            self.windowAPI.setVisible(True)
            self.windowCitySelect.setVisible(False)


        self.show()

    def window_api_button(self):
        api_key = self.api_input.text()
        if not api_key:
            QtWidgets.QMessageBox.warning(self, "Błąd", "Wprowadź API key.")
            return

        if not self.weather_api.check_api(api_key):
            QtWidgets.QMessageBox.warning(self, "Błąd", "Wprowadzony API key jest niepoprawny.")
            return

        if self.save_checkbox.isChecked():
            os.environ["WEATHER_API_KEY"] = api_key  # lub zapisz do pliku

        self.group_api.hide()
        self._on_api_ready(api_key)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()

    sys.exit(app.exec_())