import sys

from app import Generator, utils, UsageGUI
from PyQt6.QtWidgets import QApplication, QWidget

from app.utils import check_settings

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = UsageGUI.Window()
    sys.exit(app.exec())
