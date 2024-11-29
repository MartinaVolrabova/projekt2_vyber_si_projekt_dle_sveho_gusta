"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Martina Volrábová
email: martina.volrabova@seznam.cz
discord: Martina Volrábová, Martina Volrabova#!pdb1714
"""

import random

def random_digit():
    """Generate random 4-digit number with the first digit non-zero and remaining digits can include zero. Range is 0-9"""

    """Possible digits (0-9)"""
    digits = list(range(10))
    """First digit: 1-9"""
    first_digit = random.randint(1, 9)
    """Remove the first value from the list to ensure uniqueness"""
    digits.remove(first_digit)
    """Select 3 unique digits from the rest"""
    remaining_digits = random.sample(digits, 3)

    """join first digit with the other three"""
    return [first_digit] + remaining_digits

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
        #print(f"Generated list: {secret_number}")
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
