"""Mutating functions."""

__author__ = "730660760"


def manual_append(a: list[int], value: int) -> None:
    """Apend Funciton"""
    a.append(value)


def double(b: list[int]) -> None:
    """Doubles each element in the list"""
    index: int = 0
    while index < len(b):
        b[0 + index] = b[0 + index] * 2
        index += 1


# defines global variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
