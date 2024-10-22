__author__ = "730761531"

from find_max import find_and_remove_max


def test_find_and_remove_max_expected() -> None:
    """Ensures that function returns expected value"""
    a: list[int] = [1, 5, 2, 9, 7]
    assert find_and_remove_max(a) == 9


def test_find_and_remove_max_mutation() -> None:
    """Ensures that the list is mutated properly"""
    a: list[int] = [1, 5, 2, 9, 7, 9]
    find_and_remove_max(a)
    assert a == [1, 5, 2, 7]


def test_find_and_remove_max_empty_list() -> None:
    """Ensure -1 is returned when given an empty list"""
    a: list[int] = []
    assert find_and_remove_max(a) == -1
