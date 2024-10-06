"""Mutatating functions"""

__author__ = "730761531"


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(base: list[int], add: int) -> None:
    base.append(add)


def double(base: list[int]) -> None:
    count: int = 0
    while count < len(base):
        base[count] = base[count] * 2
        count += 1


double(base=list_2)

print(list_1)
print(list_2)
