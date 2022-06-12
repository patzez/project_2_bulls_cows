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


def input_number() -> int:
    while True:
        number = input("Guess a number: ")
        if number.isdecimal():
            number = int(number)
            if not check_duplicate(number):
                print("Numbers in your guess can't repeat. Try again.")
                continue
            if not check_len(number):
                print("Your guess must be 4 digits long. Try again.")
                continue
            if not check_start_number(number):
                print("Your guess can't start with 0. Try again.")
                continue
        else:
            print("Your guess must be 4-digit number with unique numbers and can't begin with 0!",
                  "Try again.", sep="\n")
            continue
        break
    return int(number)


def num_to_list(number: int) -> list:
    return [int(i) for i in str(number)]


def count_bulls_cows(generated: int, guess: int) -> tuple:
    bulls = 0
    cows = 0
    generated_list = num_to_list(generated)
    guess_list = num_to_list(guess)

    for i, j in zip(generated_list, guess_list):
        if j in generated_list:
            if i == j:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def num_of_tries() -> int:
    while True:
        tries = input("Enter number of tries: ")
        if tries.isnumeric() and int(tries) > 0:
            break
        else:
            print("Number of tries must be a whole number greater than 0!")
            continue
    return int(tries)


def play_bulls_and_cows():
    while True:
        number = generate_number()
        tries = num_of_tries()

        while tries > 0:
            guess = input_number()
            b_and_c = count_bulls_cows(number, guess)
            print(f"{b_and_c[0]} bulls, {b_and_c[0]} cows")

            if b_and_c[0] == 4:
                print("You guessed right!")
                break

            tries -= 1

        again = input("Play again? [y / n]")

        if again == "y":
            continue
        elif again == "n":
            break
        else:
            print("Invalid imput!")









# vyber = input_number()
# generovane = generate_number()
# print(type(vyber),
#       num_to_list(vyber))
# print(type(generovane),
#       num_to_list(generovane))
# print(list(zip(num_to_list(vyber), num_to_list(generovane))))
# print(type(count_bulls_cows(generovane, vyber)),
#       count_bulls_cows(generovane, vyber))
