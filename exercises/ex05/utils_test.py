"""Unit Test for Utils EX05"""

author__ = "730660760"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest

# imports all the functions and pytest


# only_evens function tests:


def test_only_evens_edge_case() -> None:
    """As we are using remainder division by 2, we are checking how all 0's is handled"""
    assert only_evens([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]


# tests an edge, where all the values are equal and equivalent ot 0
# although 0 is even, as we are using divion it is good idea to check
# this works properly


def test_only_does_not_mutate_input() -> None:
    """Testing mutation behavior"""
    x = [3, 3, 4, 4, 5, 6, 7]
    only_evens(x)
    assert x == [3, 3, 4, 4, 5, 6, 7]


# this tests that the input list does not get mutated
# compares the value of x, the input list, before and
# after only_evens is called


def test_only_evens_produces_proper_return_value() -> None:
    """Tests if return value is correct"""
    x = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(x) == [2, 4, 6]


# this tests that return value of funciton, is the subset
# of the input list of its even integer values


# sub Function Tests:


def test_sub_edge_case() -> None:
    """Test edge case, where end value and start value are equal"""
    list_sub = [1, 2, 3, 4, 5, 6]
    a = 1
    b = 1
    assert sub(list_sub, a, b) == []
    # tests edge cause were the start and end values are equal
    # as we wanted the function to be non inclusive it should return
    # the empty list


def test_sub_does_not_mutate_input() -> None:
    """Checks if test sub correctly does not mutate its input"""
    list_sub = [1, 2, 3, 5, 6, 9]
    a = 1
    b = 2
    sub(list_sub, a, b)
    assert list_sub == [1, 2, 3, 5, 6, 9]

    # checks if the input list is not mutated, by comparing list_sub
    # value before and after sub is called


def test_sub_return_value() -> None:
    """tests if sub has the proper return value"""
    list_sub = [3, 4, 5, 6, 8, 9, 20]
    a = 1
    b = 4
    assert sub(list_sub, a, b) == [4, 5, 6]

    # checks if the output of sub is a list of integers
    # in list_sub contained within a and b


# add_at_index function tests:


def test_add_at_index_raises_indexerror():
    """tests that add_at_index reaises an IndexError for invalid index"""
    list_z = [1, 3, 5, 6]
    value = 10
    index = 5
    with pytest.raises(IndexError):
        add_at_index(list_z, value, index)
    # uses the pytest to determine if when an index that is out of range is inputted
    # returns the proper error message


def test_add_at_index_mutates_input_list() -> None:
    """tests if add_at_index produces the correct return value"""
    list_z = [1, 2, 3, 4, 5, 6, 8]
    value = 7
    index = 6
    add_at_index(list_z, value, index)
    assert list_z == [1, 2, 3, 4, 5, 6, 7, 8]
    # checks if list_z is properly mutated to include the new value and the correct
    # index


def test_add_at_index_() -> None:
    list_z = [1, 2, 3, 4, 5, 6, 8]
    value = 7
    index = 6
    assert add_at_index(list_z, value, index) == None

    # checks if the return value of add_at_index is None
