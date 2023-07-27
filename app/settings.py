from pathlib import Path

setting_dict: dict = {
    "lang": 'en',
    "Lmin": 12,
    "Lmax": 20,
    "set": {
        "first_number": 0,
        "onlyLowerCase": 0,
        "usedPunctuation": 1,
        "usedDigits": 1,
    },
    "db_name": 'yDatabase.db',
}

db_file = Path(__file__).parent.parent.resolve() / 'yDatabase.db'
setting_file = Path(__file__).parent.resolve() / '/settings.py'
pswrd_file = Path(__file__).parent.parent.resolve() / 'common/pswrd.txt'
