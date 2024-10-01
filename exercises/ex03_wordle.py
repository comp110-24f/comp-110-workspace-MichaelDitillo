"""Exercise 3"""

__author__ = "730660760"


def input_guess(secret_word_len: int) -> str:
    """Checks the length of input_guess"""
    guess = input(f"Enter a {secret_word_len} character word: ")
    # prints the above message, takes the users response as a str
    while len(guess) != secret_word_len:
        # checks if the length of guess doe snot equal the length of secret_word_len
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


# returns the users guess if the len(guess) == secret_word_len
# by including {secret_word_len} we are ensuring the function works for any
# specefied secret word, and not a hardcoded length


def contains_char(secret_word: str, chr_guess: str) -> bool:
    """Contains_chr checks if the char in guess is in secret word"""
    assert len(chr_guess) == 1
    # This line checks the length of char_guess.
    # If char_guess is not exactly 1 character  an Assertion Error will be raised.
    index = 0  # indexes from 0
    while index < len(secret_word):  # less than due to zero indexing
        if secret_word[index] == chr_guess:
            return True
        index += 1  # indexes by one each time
    return False
    # the while loop continues running, as long as the index is less
    # than the length of the secret word, avoiding the infinite loop
    # if the while loop is entered, the if statement is evaluated
    # to determine if any of that letter in secret_word matches
    # the chr in chr_guess


def emojified(user_guess: str, secret: str) -> str:
    """Emojified makes a wordle like interface"""
    assert len(user_guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # defines the str by the codes which corresponds to their color emoji

    result = str()
    # defines result as an empty str
    index = 0
    # indexs from 0

    while index < len(user_guess):  # less than due to 0 indexing
        if user_guess[index] == secret[index]:
            result += GREEN_BOX  # if the chr matches green added
        elif contains_char(secret, user_guess[index]):
            result += (
                YELLOW_BOX  # if the chr appears someowhere in secret yellow  added
            )
        else:
            result += (
                WHITE_BOX  # if the chr does not appear someowhere in secret red  added
            )
        index += 1

    return result
    # each time the loop is executed, a color emoji is added to the empty str result
    # and one is added to the index
    # this continues untile the index is no longer less than the len of user_guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    total_turns = 6
    current_turn = 1
    already_won = False
    # Game state variables
    # user starts with 6 guess
    # begins on the first guess
    # the user starts the game having not yet won

    while current_turn <= total_turns and not already_won:
        print(f"=== Turn {current_turn}/{total_turns} ===")
        guess = input_guess(len(secret))
        emoji_result = emojified(guess, secret)
        print(emoji_result)
        # the loop is entered, as long as the user has not used all of there turns
        # and has not already won the game

        if guess == secret:
            already_won = True
        # checks if you user has won by entering the word which matches the secret word
        # if they are the same
        # the while loop is then broken, as already_won now has a True value
        current_turn += 1
        # indexes by one

    if already_won:
        print((f"You won in {current_turn - 1}/{total_turns} turns!"))
    # if already_won is True, the bellow method prints, telling the user
    # that they won in x/6 attempts
    else:
        print(f"X/{total_turns} - Sorry, try again tomorrow!")
    # if the user does not get the word in 6 attepmts the above message is printed


if __name__ == "__main__":
    main(secret="codes")
