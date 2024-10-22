"""EX05 - Test File"""

__author__ = "730761531"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_returns() -> None:
    """Tests if only_evens returns the right thing"""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(a) == [2, 4, 6]


def test_only_evens_doesnt_mutate() -> None:
    """Tests if only_evens doesn't mutate the input list"""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5, 6]


def test_only_evens_empty_list() -> None:
    """Tests if only_evens returns an empty list if given an empty list"""
    a: list[int] = []
    assert only_evens(a) == []


def test_sub_returns() -> None:
    """Tests if sub returns the correct value"""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a, 2, 5) == [3, 4, 5]


def test_sub_doesnt_mutate() -> None:
    """Tests if sub doesnt mutate input list"""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    sub(a, 2, 5)
    assert a == [1, 2, 3, 4, 5, 6]


def test_sub_empty_list() -> None:
    """Tests if sub returns an empty list if given an empty list"""
    a: list[int] = []
    assert sub(a, -1, 3) == []


def test_add_at_index_return() -> None:
    """Ensures that add_at_index doesnt return anything"""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert add_at_index(a, 3, 5) == None


def test_add_at_index_mutates() -> None:
    """Tests if add_at_index properly mutates the input list"""
    a: list[int] = [1, 2, 3, 4, 5]
    add_at_index(a, 0, 2)
    assert a == [1, 2, 0, 3, 4, 5]


def test_add_at_index_index_too_large() -> None:
    """Tests if add_at index raises an IndexError if index > len(list)"""
    a: list[int] = [1, 2, 3, 4, 5]

    with pytest.raises(IndexError):
        add_at_index(a, 3, 20)
