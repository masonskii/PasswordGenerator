import sys
from typing import Any

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QIODevice, Qt
from PyQt6.QtWidgets import QWidget, QApplication

from app import utils, UsageGUI
from app.GUI.login_form import Ui_login_form
from app.GUI.main_form import Ui_MainWindow


class Window(QWidget):
    """

    """

    def __init__(self):
        """

        """
        super().__init__()
        self.setting_dict = utils.check_settings()
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        self.show()

