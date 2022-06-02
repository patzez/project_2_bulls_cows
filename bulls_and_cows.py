"""
bulls_and_cows.py: Druhý projekt do Engeto Online Python Akademie

author: Patrik Zezulka
email: pat.zezulka@gmail.com
discord: patzez#8128
"""

import random


def check_start_number(number):
    if not number.startswith("0"):
        return True
    else:
        return False


def check_duplicate(number):
    if len(list(str(number))) == len(set(str(number))):
        return True
    else:
        return False


def generate_number():
    number = ""
    while True:
        while len(number) != 4:
            number += str(random.randint(0, 9))

        if not check_start_number(number) and check_duplicate(number):
            break
        else:
            continue
    return number

print(generate_number())