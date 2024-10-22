__author__ = "730761531"


def find_and_remove_max(list1: list[int]) -> int:
    largest: int
    count: int = 0

    if len(list1) == 0:
        return -1

    largest = list1[0]

    for elem in range(len(list1)):
        if list1[elem] > largest:
            largest = list1[elem]

    while count < len(list1):
        if list1[count] == largest:
            list1.pop(count)
        else:
            count += 1

    return largest


find_and_remove_max([])
