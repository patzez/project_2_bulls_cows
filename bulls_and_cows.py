"""
bulls_and_cows.py: Druhý projekt do Engeto Online Python Akademie

author: Patrik Zezulka
email: pat.zezulka@gmail.com
discord: patzez#8128
"""

import random


def main():
    separator_double = "=" * 25
    print(separator_double,
          "Hello!",
          "I have generated a random",
          "4 digit number.",
          "Let's play bulls and cows!",
          separator_double, sep="\n")
    play_bulls_and_cows()


def check_start_number(number) -> bool:
    if not str(number).startswith("0"):
        return True
    else:
        return False


def check_duplicate(number) -> bool:
    if len(list(str(number))) == len(set(str(number))):
        return True
    else:
        return False


def check_len(number) -> bool:
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
    separator = "-" * 25
    while True:
        number = input("Guess a number: ")
        if number.isdecimal():
            number = str(number)
            if not check_duplicate(number):
                print(separator,
                      "Numbers in your guess can't repeat.",
                      "Try again.",
                      separator, sep="\n")
                continue
            if not check_len(number):
                print(separator,
                      "Your guess must be 4 digits long.",
                      "Try again.",
                      separator, sep="\n")
                continue
            if not check_start_number(number):
                print(separator,
                      "Your guess can't start with 0.",
                      "Try again.",
                      separator, sep="\n")
                continue
        else:
            print(separator,
                  "Your guess must be 4-digit number, ",
                  "with unique numbers, ",
                  "that can't begin with 0!",
                  "Try again.",
                  separator, sep="\n")
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
            print("Number of tries must be",
                  "a whole number greater than 0!",
                  sep="\n")
            continue
    return int(tries)


def play_again() -> bool:
    while True:
        again = input("Play again? [y / n]: ")
        if again == "y":
            return True
        elif again == "n":
            return False
        else:
            print("Invalid imput!")
            continue


def play_bulls_and_cows():
    separator = "-" * 25
    again = True
    while again:
        number = generate_number()
        tries = num_of_tries()
        print(separator)

        while tries > 0:
            guess = input_number()
            b_and_c = count_bulls_cows(number, guess)
            print(separator,
                  f"{b_and_c[0]} bulls, {b_and_c[1]} cows",
                  sep="\n")

            if b_and_c[0] == 4:
                print(separator,
                      "You guessed right!",
                      f"The number was: {number}",
                      separator, sep="\n")
                break

            tries -= 1
            print(f"Remaining tries: {tries}",
                  separator, sep="\n")
        else:
            print("You ran out of tries!",
                  f"The number was: {number}",
                  "You have lost! :(",
                  separator, sep="\n")

        again = play_again()


if __name__ == "__main__":
    main()