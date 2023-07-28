import sys

from app import UsageGUI
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = UsageGUI.Window()
    sys.exit(app.exec())
