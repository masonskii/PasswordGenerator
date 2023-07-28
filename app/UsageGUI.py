import datetime
import numpy as np
import string
from PyQt6 import QtGui
from PyQt6.QtGui import QTextCharFormat, QTextCursor, QColor
from PyQt6.QtWidgets import QMainWindow
from app import Generator, utils, settings
from app.GUI.main_form import Ui_MainWindow
from common.colors import css_colors

gen_pass = []


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setting_dict = utils.check_settings()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ButtonGenerate.clicked.connect(self.generated)
        self.show()

        self.gen = Generator.Generator(self.setting_dict)
        self.Logging(f'<span style="color: {css_colors["OliveDrab"]};"> {utils.check_or_create_files()} </span>')
        self.Logging(f'<span style="color: {css_colors["OliveDrab"]};"> current settings : <pre style="color:' +
                     f' {css_colors["MidnightBlue"]};">{utils.formated_json(self.setting_dict)}</pre> </span>')

    def generated(self) -> None:
        if len(gen_pass) > 0:
            model = QtGui.QStandardItemModel()
            self.ui.listPassword.setModel(model)
            for i in gen_pass:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        password, code = self.gen.generate(self.setting_dict['Lmin'],
                                           self.setting_dict['Lmax'])
        if code == -1:
            self.Logging(password)
        else:
            gen_pass.append(password)
            self.ui.TextBoxGenerate.setText(password)
            self.Logging(
                f'<span style="color: {css_colors["OliveDrab"]};">generated new password: <span style="color:' +
                f' {css_colors["MidnightBlue"]};">length = {len(password)}</span> </span><br>')
            s, t = self.gen.check_password_strength(password)
            t, msg_time = self.gen.automatic_convert_seconds(t)
            if s <= 60:
                self.Logging(f'<span style="color: {css_colors["Olive"]};"> strength: '
                             f'<span style="color: {css_colors["IndianRed"]};"> {s}</span>'
                             f'<span style="color: {css_colors["Olive"]};"> time to hack: '
                             f'<span style="color: {css_colors["IndianRed"]};"> {t}'
                             f'<span style="color: {css_colors["Olive"]}:"> {msg_time} </span></span><br>')
            else:
                self.Logging(f'<span style="color: {css_colors["Olive"]};"> strength: '
                             f'<span style="color: {css_colors["ForestGreen"]};"> {s} </span>'
                             f'<span style="color: {css_colors["Olive"]};"> time to hack: '
                             f'<span style="color: {css_colors["ForestGreen"]};"> {t}'
                             f'<span style="color: {css_colors["Olive"]}:"> {msg_time} </span></span><br>')

    def Logging(self, text: str) -> None:
        """
        self.ui.LoggerText.append(f"{datetime.datetime.now().time()} ||{text}")
        """

        self.ui.LoggerText.insertHtml(
            f'<span style="color:{css_colors["SteelBlue"]};"> {datetime.datetime.now().time()} : '
            f'{text}</span><br>'
        )
