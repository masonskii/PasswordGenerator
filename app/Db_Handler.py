import sqlite3
from sqlite3 import Error

sql_create_login_table = """ CREATE TABLE IF NOT EXISTS login (
                                    id integer PRIMARY KEY,
                                    login text NOT NULL,
                                    password text,
                                    data text
                                ); """

sql_create_password_table = """CREATE TABLE IF NOT EXISTS password (
                                id integer PRIMARY KEY,
                                login text,
                                password text NOT NULL,
                                FOREIGN KEY (login_id) REFERENCES login (id)
                            );"""

class Db_handler:
    def __init__(self) -> None:
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

    def create_table(self, create_table_sql) -> bool:
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
