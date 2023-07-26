import datetime
import string

import numpy as np
from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow

from app import Generator, utils, settings
from app.GUI.main_form import Ui_MainWindow

gen_pass = []


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ButtonGenerate.clicked.connect(self.generated)
        self.show()

        self.gen = Generator.Generator()
        self.Logging(utils.check_or_create_files())

    def generated(self) -> None:
        if len(gen_pass) > 0:
            model = QtGui.QStandardItemModel()
            self.ui.listPassword.setModel(model)
            for i in gen_pass:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        password, code = self.gen.generate(settings.setting_dict['Lmin'],
                                           settings.setting_dict['Lmax'])
        if code == -1:
            self.Logging(password)
        else:
            gen_pass.append(password)
            self.ui.TextBoxGenerate.setText(password)
            self.Logging(f"generated new password, length {len(password)}")


    def Logging(self, text: str) -> None:
        self.ui.LoggerText.append(f"{datetime.datetime.now().time()} ||{text}\n")
