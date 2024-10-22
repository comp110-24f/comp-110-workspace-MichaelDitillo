"""EX05S File Skeleton Functions"""

__author__ = "730660760"


def only_evens(list_x: list[int]) -> list[int]:
    """only_even creates a list consisting of even elements from another list"""
    index: int = 0  # indexes from 0
    list_x_evens: list[int] = []  # sets list_x_evens as the empty list
    while index < len(list_x):  # avoids infininte loop
        if (
            list_x[index] % 2 == 0
        ):  # checks if the number is even, divisible by 2 with no remainder
            list_x_evens.append(
                list_x[index]
            )  # appends the empty list with the even integer
        index += 1  # indexes by one
    return list_x_evens


# reuturns the new list_x_evens, without mutating list_x


def sub(list_y: list[int], y_start: int, y_end: int) -> list[int]:
    """sub takes a list as an input, creates a new shortened list"""
    subset_list_y: list[int] = []  # sets subset_list_y as the empty list
    if len(list_y) == 0 or y_start >= len(list_y) or y_end <= 0:
        return []  # deals with the given edge cases
    if y_start < 0:
        y_start = 0
    # since lists utilize 0 indexing, the first element in the list is always
    # index 0, a negative y_start would bellow this value, so we can simply
    # assigned any negative y_starts, as beginning from the 0 index

    if y_end > len(list_y):
        y_end = len(list_y)
    # similar logic to y_start, only  now if a number that is larger then length of
    # the list is inputed, we can simply equate y_end to the leng of list_y
    # and still encapsulate the same upper bound

    for y in range(y_start, y_end):  # for loop bounded by y_start and y_end
        subset_list_y.append(
            list_y[y]
        )  # appends the empty set with the values in the above range
    return subset_list_y  # returns the appended, subset_list_y


def add_at_index(list_z: list[int], value: int, index_z: int) -> None:
    """add_at_index allows a value to be added to a list at a specefic index"""
    if len(list_z) < index_z or index_z < 0:  # edge cases
        raise IndexError(
            "Index is out of bounds for the input list"
        )  # raises this index error
    list_z.append(0)  # 0 is a placeholder value increasing the len by one
    for z in range(len(list_z) - 1, index_z, -1):
        # len(list_z) - 1, calculates the last index of the list before adding
        # the placeholder
        # inde_z is where the new value is inserted
        # -1, indicates the loop is counting backward by 1
        list_z[z] = list_z[z - 1]
        # In each iteration, the current position z is filled with the value from the
        # previous position z - 1.This effectively shifts all elements to the right,
        # creating a gap at index_z.
    list_z[index_z] = value
    # After the loop all the elements to the right, making "room"
    # for new value
    # This line assigns the value to that index, completing the insertion.
