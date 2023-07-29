from pathlib import Path

"""
setting_dict: dict = {
    "lang": None,
    "Lmin": None,
    "Lmax": None,
    "set": {
        "first_number": None,
        "onlyLowerCase": None,
        "usedPunctuation": None,
        "usedDigits": None,
    },
}
"""

db_file = Path(__file__).parent.parent.resolve() / 'yDatabase.db'
setting_file = Path(__file__).parent.parent.resolve() / 'settings.json'
pswrd_file = Path(__file__).parent.parent.resolve() / 'common/pswrd.txt'

"""SQL QUERY"""
sql_create_login_table = (""" CREATE TABLE IF NOT EXISTS login (
                                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                    login TEXT NOT NULL,
                                    password TEXT
                                ); """
                          )

sql_create_password_table = ("""CREATE TABLE IF NOT EXISTS password (
                                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
                                login TEXT,
                                password TEXT NOT NULL,
                                strength TEXT NOT NULL,
                                TTH TEXT NOT NULL,
                                FOREIGN KEY (id) REFERENCES login (id)
                                );"""
                             )