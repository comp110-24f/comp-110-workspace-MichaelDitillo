"""Challange Question2"""

__author__ = "730660760"


def guess_a_number() -> None:
    """Compares users guess to a secret number"""
    secret: int = 7
    guess: int = int(input("Guess a number:"))
    # takes the number the user guesses and save sit as an int
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    else:
        print("Your guess was too low! The secret number is " + str(secret))
    # checks the relation of the guessed value to the secret number and returns a phrase
    # if correct prints you got it
    # if incorrect says if its higher or lower and reveals the secret number


if __name__ == "__main__":
    guess_a_number()
