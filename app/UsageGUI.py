import datetime
import decimal
from typing import Any

import numpy as np
import string
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import QPropertyAnimation, QPoint, Qt
from PyQt6.QtGui import QTextCharFormat, QTextCursor, QColor
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from app import Generator, utils, settings, login_formGUI
from app.Db_Handler import Db_handler
from app.GUI.main_form import Ui_MainWindow
from app.settings import db_file
from common.colors import css_colors

gen_pass = []


class Window(QMainWindow):
    """

    """

    def __init__(self):
        """

        """
        super().__init__()
        self.model = None
        self.setting_dict = utils.check_settings()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ButtonGenerate.clicked.connect(self.generated)
        self.ui.TextBoxGenerate.textChanged.connect(self.checking_changed_text)
        self.show()

        self.gen = Generator.Generator(self.setting_dict)
        self.Logging(f'<span style="color: {css_colors["OliveDrab"]};"> {utils.check_or_create_files()} </span>')
        self.Logging(f'<span style="color: {css_colors["OliveDrab"]};"> current settings : <pre style="color:' +
                     f' {css_colors["MidnightBlue"]};">{utils.formated_json(self.setting_dict)}</pre> </span>')
        self.db_handler = Db_handler()

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('yDatabase.db')
        self.ui.tableUserPassword.setColumnCount(5)
        self.ui.tableUserPassword.setColumnWidth(0, 50)
        self.ui.tableUserPassword.setColumnWidth(1, 250)
        self.ui.tableUserPassword.setColumnWidth(2, 500)
        self.ui.tableUserPassword.setColumnWidth(3, 500)
        self.ui.tableUserPassword.setColumnWidth(4, 500)
        # self.ui.tableUserPassword.itemChanged.connect(self.table_save)
        self.load_dataset()

    """
    def table_save(self):
        for currentQTableWidgetItem in self.ui.tableUserPassword.selectedItems():
            id = self.ui.tableUserPassword.item(currentQTableWidgetItem.row(), 0).text()
            self.db_handler.changed_login("password", [id, self.ui.tableUserPassword.item(currentQTableWidgetItem.row(), 1).text()])
    """
    def load_dataset(self):
        dataset = self.db_handler.load_dataset("password")
        self.ui.tableUserPassword.setRowCount(len(dataset.columns.values.tolist()))
        self.ui.tableUserPassword.setHorizontalHeaderLabels(dataset.columns.values.tolist())
        for i, row in dataset.iterrows():
            self.ui.tableUserPassword.setRowCount(self.ui.tableUserPassword.rowCount() + 1)
            for j in range(self.ui.tableUserPassword.columnCount()):
                self.ui.tableUserPassword.setItem(i, j, QTableWidgetItem(str(row[j])))
    """
    def add_value_to_table(self, dataset):
        dataset = self.db_handler.load_dataset("password")
        self.ui.tableUserPassword.setRowCount(len(dataset.columns.values.tolist()))
        self.ui.tableUserPassword.setRowCount(self.ui.tableUserPassword.rowCount() + 1)
        self.ui.tableUserPassword.setItem(dataset.iterrows()[len(dataset.columns.values.tolist()) - 1], self.ui.tableUserPassword.columnCount() + 1,
                                          QTableWidgetItem(str(dataset)))
    """
    def generated(self) -> None or Any:
        """

        :return:
        """
        password, code = self.gen.generate(self.setting_dict['Lmin'],
                                           self.setting_dict['Lmax'])
        if code == -1:
            self.Logging(password)
        else:
            s, t = self.gen.check_password_strength(password)
            t, msg_time = self.gen.automatic_convert_seconds(t)
            self.db_handler.insert_value_in_table("password", ["", password, s, str(t) + str(" " + msg_time)])
            self.load_dataset()
            self.ui.TextBoxGenerate.setText(password)

    def checking_changed_text(self) -> None or Any:
        """

        :return:
        """
        if self.ui.TextBoxGenerate.toPlainText():
            s, t = self.gen.check_password_strength(self.ui.TextBoxGenerate.toPlainText())
            t, msg_time = self.gen.automatic_convert_seconds(t)
            if 0 <= s <= 20:
                self.ui.TextStrenght.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                    f'<span style="color: {css_colors["Crimson"]};"> {s}</span><br>'
                )
                self.ui.TextTtH.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                    f'<span style="color: {css_colors["Crimson"]};"> {t}'
                    f'<span style="color: {css_colors["Crimson"]}:"> {msg_time} </span></span><br>'
                )
            if 20 <= s <= 40:
                self.ui.TextStrenght.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                    f'<span style="color: {css_colors["Coral"]};"> {s}</span><br>'
                )
                self.ui.TextTtH.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                    f'<span style="color: {css_colors["Coral"]};"> {t}'
                    f'<span style="color: {css_colors["Coral"]}:"> {msg_time} </span></span><br>'
                )
            if 40 <= s <= 60:
                self.ui.TextStrenght.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                    f'<span style="color: {css_colors["Khaki"]};"> {s}</span><br>'
                )
                self.ui.TextTtH.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                    f'<span style="color: {css_colors["Khaki"]};"> {t}'
                    f'<span style="color: {css_colors["Khaki"]}:"> {msg_time} </span></span><br>'
                )
            if 60 <= s <= 80:
                self.ui.TextStrenght.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                    f'<span style="color: {css_colors["GreenYellow"]};"> {s}</span><br>'
                )
                self.ui.TextTtH.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                    f'<span style="color: {css_colors["GreenYellow"]};"> {t}'
                    f'<span style="color: {css_colors["GreenYellow"]}:"> {msg_time} </span></span><br>'
                )
            if s >= 80:
                self.ui.TextStrenght.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> strength: '
                    f'<span style="color: {css_colors["LawnGreen"]};"> {s}</span><br>'
                )
                self.ui.TextTtH.setHtml(
                    f'<span style="color: {css_colors["Chocolate"]};"> time to hack: '
                    f'<span style="color: {css_colors["LawnGreen"]};"> {t}'
                    f'<span style="color: {css_colors["LawnGreen"]}:"> {msg_time} </span></span><br>'
                )

    def Logging(self, text: str) -> None or Any:
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

    """
    def show_login(self) -> None or Any:
        self.login_form = login_formGUI.Window()
        self.login_form.ui.ButtonOk.clicked.connect(self.checking_dataset)
        self.login_form.ui.ButtonClose.clicked.connect(self.close_all)
        self.login_form.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.login_form.raise_()
        self.login_form.showNormal()

    def setTopLevelWindow(self):
        if self.windowState() != QtCore.Qt.WindowState.WindowMaximized:
            self.showMaximized()
            self.showNormal()

        else:
            self.showNormal()
            self.showMaximized()

        self.raise_()
        self.activateWindow()

    def close_all(self) -> None or Any:
        self.login_form.close()
        self.close()

    def checking_dataset(self) -> None or Any:
        if not self.login_form.ui.textLogin.toPlainText() and not self.login_form.ui.textPassword.toPlainText():
            msg = QtWidgets.QMessageBox.information(self, 'Внимание', 'Заполните поля ввода.')
        else:
            login = self.login_form.ui.textLogin.toPlainText()
            password = self.login_form.ui.textPassword.toPlainText()
            self.login_form.close()
    """
