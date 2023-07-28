import datetime
import decimal

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
    """

    """

    def __init__(self):
        """

        """
        super().__init__()
        self.setting_dict = utils.check_settings()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ButtonGenerate.clicked.connect(self.generated)
        self.ui.ButtonCheck.clicked.connect(self.checking_click)
        self.show()

        self.gen = Generator.Generator(self.setting_dict)
        self.Logging(f'<span style="color: {css_colors["OliveDrab"]};"> {utils.check_or_create_files()} </span>')
        self.Logging(f'<span style="color: {css_colors["OliveDrab"]};"> current settings : <pre style="color:' +
                     f' {css_colors["MidnightBlue"]};">{utils.formated_json(self.setting_dict)}</pre> </span>')

    def generated(self) -> None:
        """

        :return:
        """
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
            self.Adding_params(strength=s, t=t, msg_time=msg_time)

    def checking_click(self) -> None:
        if len(self.ui.ButtonCheck.text()) != 0:
            text: str = self.ui.TextBoxGenerate.toPlainText()
            s, t = self.gen.check_password_strength(text)
            t, msg_time = self.gen.automatic_convert_seconds(t)
            self.Adding_params(strength=s, t=t, msg_time=msg_time)

    def Logging(self, text: str) -> None:
        """

        :param text:
        :return:
        """
        """
        self.ui.LoggerText.append(f"{datetime.datetime.now().time()} ||{text}")
        """
        self.ui.LoggerText.insertHtml(
            f'<span style="color:{css_colors["SteelBlue"]};"> {datetime.datetime.now().time()} : '
            f'{text}</span><br>'
        )

    def Adding_params(self, strength: np.float64, t: int, msg_time: str) -> None:
        """

        :param strength:
        :param t:
        :param msg_time:
        :return:
        """
        if 0 <= strength <= 20:
            self.ui.TextStrenght.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                f'<span style="color: {css_colors["Crimson"]};"> {strength}</span><br>'
            )
            self.ui.TextTtH.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                f'<span style="color: {css_colors["Crimson"]};"> {t}'
                f'<span style="color: {css_colors["Crimson"]}:"> {msg_time} </span></span><br>'
            )
        if 20 <= strength <= 40:
            self.ui.TextStrenght.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                f'<span style="color: {css_colors["Coral"]};"> {strength}</span><br>'
            )
            self.ui.TextTtH.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                f'<span style="color: {css_colors["Coral"]};"> {t}'
                f'<span style="color: {css_colors["Coral"]}:"> {msg_time} </span></span><br>'
            )
        if 40 <= strength <= 60:
            self.ui.TextStrenght.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                f'<span style="color: {css_colors["Khaki"]};"> {strength}</span><br>'
            )
            self.ui.TextTtH.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                f'<span style="color: {css_colors["Khaki"]};"> {t}'
                f'<span style="color: {css_colors["Khaki"]}:"> {msg_time} </span></span><br>'
            )
        if 60 <= strength <= 80:
            self.ui.TextStrenght.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                f'<span style="color: {css_colors["GreenYellow"]};"> {strength}</span><br>'
            )
            self.ui.TextTtH.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                f'<span style="color: {css_colors["GreenYellow"]};"> {t}'
                f'<span style="color: {css_colors["GreenYellow"]}:"> {msg_time} </span></span><br>'
            )
        if strength >= 80:
            self.ui.TextStrenght.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                f'<span style="color: {css_colors["LawnGreen"]};"> {strength}</span><br>'
            )
            self.ui.TextTtH.setHtml(
                f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                f'<span style="color: {css_colors["LawnGreen"]};"> {t}'
                f'<span style="color: {css_colors["LawnGreen"]}:"> {msg_time} </span></span><br>'
            )
