"""Excercise 6 Utility Functions"""

__author__ = "730660760"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of an input dictionary"""
    repeated_values: list[str] = []  # Creates an empty list
    for key in x:  # loops thorugh x
        values = x[key]  # sets values as each key value for x
        if values in repeated_values:  # checks if values is in repeated values
            raise KeyError("Cannot repeated key values in input dictionary!")
            # raises the above error if someone inputs a dictionary which has duplicate
            # values
        repeated_values.append(values)
        # as the for loop iterates through x, the values of x are assigned to values
        # and later appended to repeated_value
        # if the value is already found in repeated_values, then the error message
        # is raisesd
    y: dict[str, str] = {}  # creates local variable y as a dict
    for key_x in x:  # iterates through x
        key_y = x[key_x]  # y's key are given the value of x's values
        y[key_y] = key_x  # y's values are given the alue of x's keys
    return y


def favorite_color(favorite_colors: dict[str, str]) -> str:
    """Takes a dicitonary of names and colors, and returns the most occuring color"""
    totals: dict[str, int] = {}
    most_popular_color: str = ""
    most_popular: int = 0
    for key in favorite_colors:  # iterates over favorite_colors
        color = favorite_colors[
            key
        ]  # color is defined as the values of favorite_colors
        if color in totals:
            totals[color] += 1
            # if color is found already in totals, its corresponding key values
            # increase by one
        else:
            totals[color] = 1
            # if the color is not already in totals, it is added as a new key
            # and assigned a value of 1
        for color in totals:
            count = totals[color]
            # iterates through totals, declares count as the key values
            # associated with totals
            if count > most_popular:
                # most_popular is set initially at zero, and is compared to count
                most_popular = count
                # if count is larger than current value of most_popular, it takes
                # on the value of count
                most_popular_color = color
                # most_popular_color, takes on the value of color, which is the key
                # for totals, associated with the current value of count

    return most_popular_color


def count(values: list[str]) -> dict[str, int]:
    """Takes a list returns a dictionary of items and their number of occurrences"""
    frequencies: dict[str, int] = {}
    for item in values:
        # iterates through values
        if item in frequencies:
            # checks if item in values is a key in frequencies
            frequencies[item] += 1
            # if yes, the value associated with the key: item in frequencies
            # increases by one
        else:
            frequencies[item] = 1
            # if it has not been found, the iteam is added as a new key
            # to frequencies and its value is increased by one
    return frequencies


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Takes a list of words, organizes by first letter in a dictionary"""
    alphabetized_list: dict[str, list[str]] = {}
    for item in words:
        letter = item[0].lower()
        # declares letter as having the value of lowercase first letter
        # of the key: item in words
        if letter in alphabetized_list:
            alphabetized_list[letter].append(item)
        # if this letter is found already instide the list, the word item from words
        # is appended to the value of alphabetized_list for that letter key
        else:
            alphabetized_list[letter] = []
            alphabetized_list[letter].append(item)
        # if this letter is not found already in the list, a new list is initailized,
        # at the key of the new letter, and the associated item, or words beginning
        # with that letter is appended the value of alphabeitized_list for that letter
        # key
    return alphabetized_list


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates a dictionary of attendence for students on each day"""
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = []
        attendance[day].append(student)


# First checks if the specefied day exists in the attendence dictionary
# if the day exists, it checks if student is already listed for that
# day, to make sure that a student is not double counted in attendence
# for that day. If not, the student is appended to the list for that day.
# if the day does not exist in the dictionary, a new entry is created as an empty
# list, which is then appended with the student in attendence that day
# creating a new key and value in the dictionary
