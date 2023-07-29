import sys

from PyQt6 import QtCore
from PyQt6.QtCore import QIODevice

from app import UsageGUI
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    file = QtCore.QFile(r"assets/buttons.qss")
    file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text)
    stream = QtCore.QTextStream(file)
    app = QApplication(sys.argv)
    app.setStyleSheet(stream.readAll())
    MainWindow = UsageGUI.Window()
    sys.exit(app.exec())
