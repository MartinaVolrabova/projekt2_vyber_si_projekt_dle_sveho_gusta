"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Martina Volrábova
email: martina.volrabova@seznam.cz
discord: Martina Volrabová Martina Volrabova#!pdb1714
"""



"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Martina Volrábova
email: martina.volrabova@seznam.cz
discord: Martina Svetr#4490
"""

import random

def random_digit():
    """Generate random 4-digit number with the first digit non-zero and remaining digits can include zero. Range is 0-9"""
    digits = list(range(10))
    random.shuffle(digits)
    """ Get random digit from 1 to 9 avoiding 0 as a first digit"""
    first_digit = digits.pop(digits.index(random.choice(digits[1:]))),
    """ return first digit with non-zero value and extend it with three random digits"""
    return [first_digit] + digits[:3]

def get_bulls_and_cows(secret, guess):
    """Return the number of Bulls and Cows for the given secret and guess."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum((min(secret.count(x), guess.count(x)) for x in set(guess))) - bulls
    return bulls, cows

"""Check if the guess is valid (4 digits, no duplicates, no zero)."""
def is_valid_guess(guess):
    if len(guess) != 4:
        return False, "The value must contain exactly 4 digits."
    if not guess.isdigit():
        return False, "The value must contain digits only."
    if guess[0] == '0':
        return False, "The value must not start with zero."
    if len(set(guess)) != 4:
        return False, "Digits must be unique."
    return True, ""

def play_game():
    secret_number = random_digit()
    attempts = 0
    separator = '-----------------------------------------------'
    print("Hi there!")
    print(separator)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)

    while True:
        guess = input("Enter a number: ")
        attempts += 1
        is_valid, error_message = is_valid_guess(guess)
        if not is_valid:
            print(error_message)
            continue 

        guess = [int(digit) for digit in guess]
        bulls, cows = get_bulls_and_cows(secret_number, guess)


        bull_answer = "Bull" if bulls == 1 else "Bulls"
        cow_answer = "Cow" if cows == 1 else "Cows"

        print(f"{bulls} {bull_answer}, {cows} {cow_answer}")
        print(separator)

        if bulls == 4:
            print(f"Correct, you've guessed the right number {secret_number} in {attempts} guesses!")
            break

if __name__ == "__main__":
    play_game()
