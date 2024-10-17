"""EX04"""

__author__ = "730660760"


def all(num_list: list[int], value: int) -> bool:
    """All Function: Looks if given int is in all of list[int]"""
    if len(num_list) == 0:
        return False
    index: int = 0
    while index < len(num_list):
        if num_list[index] != value:
            return False
        index += 1
    return True


# All indexes from 0, if the index is less than the length of the list
# the while loop will evaluate, which starts an if loop, which looks
# if the given input does appears in the first integer of the list,
# contiues doing this for the whole list, if a always =
# values True is returned, if at any point the if condition
# is met, returns false


def max(num_list2: list[int]) -> int:
    """Finds Max num in list"""
    if len(num_list2) == 0:
        raise ValueError("max() arg is an empty List")

    index: int = 0
    max_value: int = num_list2[0]

    while index < len(num_list2):
        if num_list2[index] > max_value:
            max_value = num_list2[index]
        index += 1

    return max_value


# First checkes if the len of the list is 0, if it is the above
# error message is raised, if numlist is not empty, the
# max_value is assigned the value of the first element in
# num_list, then from 0 num list is indexed through, comparing the
# the next element in num_list to the value of max_value, if larger
# then max_value takes on the larger value, and this continues
# until num_list has been fully indexed through


def is_equal(x: list[int], y: list[int]) -> bool:
    """Compares if two lists are equal"""
    if x != y:
        return False
    return True


# sipmply determines if list x and y are not equal
# if not equal False is return, if equal the loop is exited and True
# is returned


def extend(a: list[int], b: list[int]) -> None:
    """Adds all the elements list b to a"""
    index: int = 0
    while index < len(b):
        a.append(b[index])
        index += 1


# Extend indexes from zero through all of list b
# takes each element in b and appends each one
# to index a
