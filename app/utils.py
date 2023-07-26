import json
import os

import numpy as np

from .settings import setting_dict, setting_file


def difference_check_length(Lmin: np.int64, Lmax: np.int64) -> bool:
    return Lmin > Lmax


def change_settings() -> bool:
    pass


def rewrite_json() -> str:
    try:
        res: str = ""
        with open(setting_file, 'w') as f:
            json.dump(setting_dict, f)
            res = "Successfully rewrite json"
            return res
    except FileNotFoundError:
        res = "The 'docs' directory does not exist"
        return res


def check_settings() -> str:
    try:
        with open(setting_file, 'r') as f:
            rel = json.load(f)
            res: str = ""
            if rel['lang'] != setting_dict['lang']:
                setting_dict['lang'] = rel['lang']
                res += f'lang switched from {setting_dict["lang"]} to {rel["lang"]}\n'
            if rel['Lmin'] != setting_dict['Lmin']:
                setting_dict['Lmin'] = rel['Lmin']
                res += f'Lmin switched from {setting_dict["Lmin"]} to {rel["Lmin"]}\n'
            if rel['Lmax'] != setting_dict['Lmax']:
                setting_dict['Lmax'] = rel['Lmax']
                res += f'Lmax switched from {setting_dict["Lmax"]} to {rel["Lmax"]}\n'
            if rel['set']['first_number'] != setting_dict['set']['first_number']:
                setting_dict['set']['first_number'] = rel['set']['first_number']
                res += f'First Number switched from {setting_dict["set"]["first_number"]} to ' \
                       f'{rel["set"]["first_number"]}\n'
            if rel['set']['onlyLowerCase'] != setting_dict['set']['onlyLowerCase']:
                setting_dict['set']['onlyLowerCase'] = rel['set']['onlyLowerCase']
                res += f'onlyLowerCase switched from {setting_dict["set"]["onlyLowerCase"]}' \
                       f' to {rel["set"]["onlyLowerCase"]}\n'
            if rel['set']['usedPunctuation'] != setting_dict['set']['usedPunctuation']:
                setting_dict['set']['usedPunctuation'] = rel['set']['usedPunctuation']
                res += f'usedPunctuation switched from {setting_dict["set"]["usedPunctuation"]}' \
                       f' to {rel["set"]["usedPunctuation"]}\n'
            if rel['set']['usedDigits'] != setting_dict['set']['usedDigits']:
                setting_dict['set']['usedDigits'] = rel['set']['usedDigits']
                res += f'usedDigits switched from {setting_dict["set"]["usedDigits"]}' \
                       f' to {rel["set"]["usedDigits"]}\n'
            if rel['db_name'] != setting_dict['db_name']:
                setting_dict['db_name'] = rel['db_name']
                res += f'db_name switched from {setting_dict["db_name"]} to {rel["db_name"]}\n'
        return res
    except FileNotFoundError:
        res: str = "The 'docs' directory does not exist\n"
        return res


def check_or_create_files() -> str:
    if os.path.exists(setting_dict['db_name']) and os.path.exists(setting_file):
        res: str = "setting file found and database found\n"
        return res
    else:
        res: str = "database or setting file not found ... creating\n"
        # Create an empty file
        try:
            if not os.path.exists(setting_dict['db_name']):
                # Open the file in write mode to create it
                with open(setting_dict['db_name'], 'w') as file:
                    pass
                res += "database created!\n"
            if not os.path.exists(setting_file):
                # Open the file in write mode to create it
                with open(setting_file, 'w') as file:
                    json.dump(setting_dict, file)
                    pass
                res += "setting file created!\n"
            return res
        except IOError:
            res = "An error occurred while creating the file.\n"
            return res


def connect_to_database() -> bool:
    pass
