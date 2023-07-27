import datetime
import numpy as np
import random
import secrets
import string
import re
import math
import decimal
from itertools import dropwhile

from .settings import setting_dict, pswrd_file


class Generator:
    def __init__(self):
        self.apl = str()

    def generate(self, min: np.int64, max: np.int64) -> list[str | np.int8]:
        try:
            if not self.check_values(max - min):
                raise Exception("value length <= 1")
        except Exception as e:
            return [self.new_error(e.__str__()), -1]

        if setting_dict['set']['onlyLowerCase']:
            self.apl: str = string.ascii_lowercase
        else:
            self.apl: str = string.ascii_letters

        if setting_dict['set']['usedDigits']:
            self.apl += string.digits
        if setting_dict['set']['usedPunctuation']:
            self.apl += string.punctuation

        if setting_dict['set']['first_number']:
            first_letter: str = secrets.choice(string.digits)
        else:
            first_letter: str = secrets.choice(string.ascii_letters + string.punctuation)

        new_password: str = \
            first_letter + str().join(secrets.choice(self.apl)
                                      for _ in np.arange(random.randint(min, max)))
        error_msg, isValidate = self.validate_by_common_list(new_password)
        if not isValidate:
            return [error_msg, -1]
        return [new_password, 0]

    @staticmethod
    def check_values(length: int) -> bool:
        return length > 1

    def validate_by_common_list(self, password) -> list[str, bool]:
        """Валидация пароля по списку самых распространенных паролей."""

        with open(pswrd_file, 'r') as f:
            for line in dropwhile(lambda x: x.startswith('#'), f):
                common = line.strip().split(':')[-1]  # выделяем сам пароль
                if password.lower() == common:
                    return ['Do not use so common password.', False]
        return ["good password", True]

    def check_password_strength(self, password: str) -> list[np.float64, np.float64]:
        # Параметры сложности пароля
        LENGTH_WEIGHT: np.int64 = 20
        DIGIT_WEIGHT: np.int64 = 25
        UPPERCASE_WEIGHT: np.int64 = 20
        LOWERCASE_WEIGHT: np.int64 = 20
        SPECIAL_CHAR_WEIGHT: np.int64 = 15

        # Шаблон регулярного выражения для проверки условий
        patterns = [
            r'.{12,}',  # Минимум 12 символов
            r'\d+',  # Минимум одна цифра
            r'[A-Z]+',  # Минимум одна заглавная буква
            r'[a-z]+',  # Минимум одна строчная буква
            r'[^a-zA-Z0-9\s]+'  # Минимум один специальный символ
        ]

        score: np.int64 = 0
        for pattern in patterns:
            if re.search(pattern, password):
                score += 1

        # Расчет сложности пароля
        length = len(password)
        strength = (score / len(patterns)) * 100
        # Оценка времени взлома пароля
        characters = 0
        if any(re.search(pattern, password) for pattern in [r'[a-zA-Z]', r'\d', r'[^a-zA-Z0-9]']):
            characters = 96  # Общее количество возможных символов

        entropy = decimal.Decimal(characters) ** length
        time_to_crack = entropy / decimal.Decimal('2e10')
        return strength, time_to_crack

    @staticmethod
    def new_error(error_text: str) -> str:
        return "Generated error, data: " + str(datetime.datetime.now().time()) + str(" ") + error_text + " :( "
