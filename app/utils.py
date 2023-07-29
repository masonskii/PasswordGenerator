import json
from typing import Any

import numpy as np
import os

from .Db_Handler import Db_handler
from .settings import setting_file, db_file, sql_create_login_table, sql_create_password_table


def difference_check_length(Lmin: np.int64, Lmax: np.int64) -> bool:
    """

    :param Lmin:
    :param Lmax:
    :return:
    """
    return Lmin > Lmax


def change_settings() -> bool:
    """

    :return:
    """
    pass


def rewrite_json(setting_dict) -> str:
    """

    :param setting_dict:
    :return:
    """
    try:
        res: str = ""
        with open(setting_file, 'w') as f:
            json.dump(setting_dict, f)
            res = "Successfully rewrite json"
            return res
    except FileNotFoundError:
        res = "The 'docs' directory does not exist"
        return res


def check_settings() -> Any | None:
    """

    :return:
    """
    try:
        with open(setting_file, 'r') as f:
            rel = json.load(f)
        return rel
    except FileNotFoundError:
        return None


def check_or_create_files() -> str:
    """

    :return:
    """
    if os.path.exists(db_file) and os.path.exists(setting_file):
        res: str = "database found, setting file found"
    else:
        res: str = "database or setting file not found ... creating "
        # Create an empty file
        try:
            if not os.path.exists(db_file):
                # Open the file in write mode to create it
                with open(db_file, 'w') as file:
                    pass
                db = Db_handler()
                db.create_table(sql_create_login_table)
                db.create_table(sql_create_password_table)
                db.insert_value_in_table('login', ["admin", "admin"])
                res += f"database created! table  {str('{')}\n '{sql_create_login_table}\n{str('}')}\n" \
                       f"{str('{')}\n{sql_create_password_table}\n{str('}')}\nAdmin user created with login=admin, password=admin"

            if not os.path.exists(setting_file):
                # Open the file in write mode to create it
                with open(setting_file, 'w') as file:
                    json.dump(
                        {
                            "lang": "en",
                            "Lmin": 12,
                            "Lmax": 20,
                            "set": {
                                "first_number": 0,
                                "onlyLowerCase": 0,
                                "usedPunctuation": 1,
                                "usedDigits": 1
                            }
                        }, file)
                    pass
                res += "setting file created! "
        except IOError:
            res = "An error occurred while creating the file."
            return res
    return res


def formated_json(rel: dict) -> str:
    """

    :param rel:
    :return:
    """
    return json.dumps(rel, indent=4)
