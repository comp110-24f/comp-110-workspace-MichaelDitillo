"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730660760"


def input_word() -> str:
    """Input Word function allows a word to be inputted"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    # checks if length of word is 5, if yes returns the word
    else:
        print("Error: Word must contain 5 characters.")
        # if length of word != 5, prints above msg
        exit()
        #  if no the error message is printed, and the exit funciton is called
        # this exists the function, and the code stops running


def input_letter() -> str:
    """Input lette function allows letter to be inputted"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    # checks if letter is one character long, if yes returns letter
    else:
        print("Error: Character must be a single character.")
        exit()
    # if no the error message is printed, and the exit funciton is called
    # this exists the function, and the code stops running


def contains_char(word: str, letter: str) -> None:
    """Contains Character compares inputted word to inputted letter"""
    print("Searching for " + letter + " in " + word)
    # parameters of contains_char are the lette rand word variables
    # prints the searching message
    found: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        found = found + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        found = found + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        found = found + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        found = found + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        found = found + 1
    # goes character by character compares the letter to the character
    # each time it is found it prints the message where it was found
    # for each time it is true one is added to the found variable
    # this is done so the number of instances the character
    # is found in the word can be added up at the end
    if found == 0:
        print("No instances of " + letter + " found in " + word)
        # if found does not change, it means the letter did not
        # match any of the words charactes, and the above msg is printed
    if found == 1:
        print(str(found) + " instance of " + letter + " found in " + word)
    # if the letter appeared only one time, the value of found will be one
    # This causes the above message to be printed
    if found > 1:
        print(str(found) + " instances of " + letter + " found in " + word)
    # if the letter appeared more than one time, the value of found will be > 1
    # this causes the above message to be printed


def main() -> None:
    """Main function executes and relates above functions"""
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)


# main function relates the three above functions
# makes the input_lette and input_word functions
# equal to the parements contains_char
# once main is called firs input_word is executed
# then input_letter is executed
# the new values of these variables are inputed into
# the contains_char function


if __name__ == "__main__":
    main()
