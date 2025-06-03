import sys
from PyQt5 import QtWidgets, uic

class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./assets/window.ui", self)  # Ładowanie .ui
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
