"""
bulls_and_cows.py: Druhý projekt do Engeto Online Python Akademie

author: Patrik Zezulka
email: pat.zezulka@gmail.com
discord: patzez#8128
"""

import random


def check_start_number(number: int) -> bool:
    if not str(number).startswith("0"):
        return True
    else:
        return False


def check_duplicate(number: int) -> bool:
    if len(list(str(number))) == len(set(str(number))):
        return True
    else:
        return False


def check_len(number: int) -> bool:
    if len(str(number)) == 4:
        return True
    else:
        return False


def generate_number() -> int:
    while True:
        number = random.randint(1000, 9999)
        if check_start_number(number) and check_duplicate(number):
            break
        else:
            continue
    return number


def input_number():
    while True:
        number = input("Enter a number: ")
        if number.isdecimal() and check_duplicate(number) and check_len(number) and check_start_number(number):
            break
        else:
            print("Invalid input.")
            continue
    return number


vyber = input_number()
print(vyber)
print(generate_number())
