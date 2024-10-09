"""Lists utils"""

__author__ = "730761531"


def all(input_list: list[int], input_int: int) -> bool:
    idx: int = 0
    if len(input_list) == 0:
        return False
    while idx < len(input_list):  # checks each index against input_int
        if input_list[idx] != input_int:
            return False
        idx += 1
    return True


def max(input_list: list[int]) -> int:
    idx: int = 0
    largest: int = input_list[0]  # starts largest at first index

    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")

    while idx < len(input_list):  # Checks each index against largest
        if input_list[idx] > largest:
            largest = input_list[idx]
        idx += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    idx: int = 0

    if len(list1) != len(list2):  # returns false is lists have unequal length
        return False

    while idx < len(list1):  # checks each index against each other
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    idx: int = 0

    while idx < len(list2):  # iterates through each element and appends it
        list1.append(list2[idx])
        idx += 1


def main() -> None:
    return


if __name__ == "__main__":
    main()
