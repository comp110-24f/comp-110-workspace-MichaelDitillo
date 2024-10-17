"""Summing the elements of a list using different loops"""

__author__ = "730660760"


def w_sum(vals: list[float]) -> float:
    """Sum using While loop"""
    index: int = 0
    total: float = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


# Takes a list of floats
# while index < len of the list, it takes the floats in the list
# adds there value to the variable total until all elements have been summed


def f_sum(vals: list[float]) -> float:
    """Sum using for loop"""
    sum = 0.0
    for x in vals:
        sum += x
    return sum


# takes the list of floats
# x represents an arbitary element in vals
# each element in vals represent by x is then summed one by one
# and added to the sum variable


def f_range_sum(vals: list[float]) -> float:
    """Sum using for loop and range function"""
    total2: float = 0
    for idx in range(0, len(vals)):
        total2 += vals[idx]
    return total2


# takes the varialbe total: assigns it a value of 0
# uses a for loop to represent the elements in range
# adds the associated values represent by idx to total2
