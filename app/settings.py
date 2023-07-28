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
