"""Find Max CQ 7"""

__author__ = "730660760"


def find_and_remove_max(a: list[int]) -> int:
    """finds and remove max value from list"""
    if a == []:
        return -1
    # avoids creating an error for the edge case of an empty list

    index: int = 0
    max_value: int = a[0]

    while index < len(a):
        if a[index] > max_value:
            max_value = a[index]
        index += 1
    # indexes through a, max value is set as the first value in the list
    # as it indexes through max value is compared to the next integer in the
    # list, if its greater mav value takes on the higher value

    idx: int = 0

    while idx < len(a):
        if a[idx] == max_value:
            a.pop(idx)
        else:
            idx += 1
    return max_value


# index through a, sees if the max_value determined by the prior loop matches
# any of the values in the list, if true the pop function removes that value
