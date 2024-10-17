"""Max Test CQ7"""

__author__ = "730660760"


from find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    """tests function return value"""
    assert find_and_remove_max([4, 5, 6, 7, 8, 9, 10]) == 10

    # tests if find_and_remove_max returns the largest integer in the list


def test_mutates_find_and_remove_max() -> None:
    """Testing mutation behavior"""
    a = [3, 3, 4, 4, 5, 6, 7]
    find_and_remove_max(a)
    assert a == [3, 3, 4, 4, 5, 6]

    # assesses whether or not find_and_remove_max properly mutates the list


def test_all_equal_values_find_and_remove_max() -> None:
    """tests for an edge case where given list are all equal values"""
    b = [3, 3, 3, 3, 3, 3, 3]
    find_and_remove_max(b)
    assert b == []

    # assesses an edge case, where a list of integers all equal to 3 is inputed
    # to determine if the function correctly mutates b into an empty list
