import sqlite3
from sqlite3 import Error
from typing import Any

import pandas as pd

from app.settings import db_file


class Db_handler:
    """

    """

    def __init__(self) -> None:
        """

        """
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
            self.conn = sqlite3.connect(db_file)
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

    def insert_value_in_table(self, table: str, dataset: list[str or Any, str or Any]) -> None or Any:
        if table == 'login':
            try:
                self.conn = sqlite3.connect(db_file)
                df_password = pd.DataFrame(
                    {
                        "login": [dataset[0]],
                        "password": [dataset[1]]
                    }
                )
                df_password.to_sql(table, self.conn, if_exists='append', index=False)
            except Error as e:
                print(e)
            finally:
                if self.conn:
                    self.conn.close()
        if table == 'password':
            try:
                self.conn = sqlite3.connect(db_file)
                df_password = pd.DataFrame(
                    {
                        "login": [dataset[0]],
                        "password": [dataset[1]],
                        "strength": [dataset[2]],
                        "TTH": [dataset[3]]
                    }
                )
                df_password.to_sql(table, self.conn, if_exists='append', index=False)
            except Error as e:
                print(e)
            finally:
                if self.conn:
                    self.conn.close()

    def get_count_id(self, table: str or Any) -> int:
        try:
            self.conn = sqlite3.connect(db_file)
            get_data = pd.read_sql(
                f""" SELECT id FROM {table}
                """, self.conn
            )
            return len(get_data.values)
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

    def changed_login(self, table: str or Any, dataset: list):
        try:
            self.conn = sqlite3.connect(db_file)
            self.conn.execute(
                f""" UPDATE {table} SET login = {dataset[1]} WHERE id = {dataset[0]};
                """
            )
            self.conn.commit()
        finally:
            if self.conn:
                self.conn.close()

    def load_dataset(self, table: str or Any):
        try:
            self.conn = sqlite3.connect(db_file)
            dataset = pd.read_sql(f"""SELECT * FROM {table} """, self.conn)
            return dataset
        finally:
            if self.conn:
                self.conn.close()
