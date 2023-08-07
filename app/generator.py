import decimal
import secrets
import string
import numpy as np
import random
import re

from _decimal import Decimal
from typing import Tuple, Any, Union


def check_values(length: int) -> bool:
    return length > 1


def generate(min: np.int64 = 1, max: np.int64 = 99,
             only_lower_case: bool = False, used_digits: bool = True,
             used_punctuation: bool = True, first_number: bool = False) -> Union[dict, str, Any]:
    apl: str = ""
    if not check_values(max - min):
        return "value length <= 1"

    if only_lower_case:
        apl = string.ascii_lowercase
    else:
        apl = string.ascii_letters

    if used_digits:
        apl += string.digits
    if used_punctuation:
        apl += string.punctuation

    if first_number:
        first_letter: str = secrets.choice(string.digits)
    else:
        if used_punctuation:
            first_letter: str = secrets.choice(string.ascii_letters + string.punctuation)
        else:
            if only_lower_case:
                first_letter: str = secrets.choice(string.ascii_lowercase)
            else:
                first_letter: str = secrets.choice(string.ascii_letters)
    new_password: str = \
        first_letter + str().join(secrets.choice(apl)
                                  for _ in np.arange(random.randint(min, max)))
    s, t = check_password_strength(new_password)
    t, msg_time = automatic_convert_seconds(t)
    result = {
        'password': new_password,
        'strength': s,
        'time_to_hack': t,
        'time': msg_time
    }
    return result


def check_password_strength(password: str) -> tuple[float | int | Any, Decimal]:
    patterns = [
        r'.{12,}',
        r'\d+',
        r'[A-Z]+',
        r'[a-z]+',
        r'[^a-zA-Z0-9\s]+'
    ]

    score: np.int64 = 0
    for pattern in patterns:
        if re.search(pattern, password):
            score += 1
    length = len(password)
    strength = (score / len(patterns)) * 100
    characters = 0
    if any(re.search(pattern, password) for pattern in [r'[a-zA-Z]', r'\d', r'[^a-zA-Z0-9]']):
        characters = 96

    entropy = decimal.Decimal(characters) ** length
    time_to_crack = entropy / decimal.Decimal('3e10')
    return strength, time_to_crack


def automatic_convert_seconds(seconds: decimal.Decimal) -> tuple[int, str]:
    seconds = int(seconds)

    levels = [
        (60, ["second", "seconds"]),
        (3600, ["minute", "minutes"]),
        (86400, ["hour", "hours"]),
        (2592000, ["day", "days"]),
        (31536000, ["month", "months"]),
    ]

    for level, labels in levels:
        if seconds < level:
            quantity = seconds // (level // 60)
            label = labels[0] if quantity % 10 == 1 else labels[1]
            return quantity, label

    label = "year" if seconds // 3153600000 % 10 == 1 else "years"
    return seconds // 3153600000, label
