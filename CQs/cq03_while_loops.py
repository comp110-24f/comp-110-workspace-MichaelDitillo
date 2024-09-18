"""Challange Question3"""

__author__ = "730660760"


def num_instances(phrase: str, search_char: str) -> int:
    """Searches the number of a times a give letter appears in a phrase"""
    count = 0
    index = 0
    # cound and index are initially set to 0
    while index < len(phrase):
        # checks if the current index is less than the len of phrase
        # indexs are zero based, this avoids going out of len bounds
        if phrase[index] == search_char:
            # takes the new index value and finds the character
            # this new character is compared to the search_char,
            # if it is  true one is added count
            # if false one is not added
            count += 1
            # increments count by one each time it is run
        index += 1
        # increments index by one each time it is run
    return count
