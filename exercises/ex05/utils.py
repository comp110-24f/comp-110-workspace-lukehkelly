"""EX05 - List Unit Tests"""

__author__ = "730761531"


def only_evens(list1: list[int]) -> list[int]:
    output_list: list[int] = []

    for item in list1:
        if item % 2 == 0:  # Checks if item is divisible by 2
            output_list.append(item)  # adds item to output_list

    return output_list


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    output_list: list[int] = []  # empty list

    if len(input_list) == 0 or start >= len(input_list) or end <= 0:
        return output_list  # returns an empty list

    if start < 0 and end > len(
        input_list
    ):  # If statement that handles a negative start and too big of an end
        for item in input_list:
            output_list.append(item)

    elif start < 0:  # handles just a negative start
        for i in range(end):
            output_list.append(input_list[i])

    else:  # handles everything else
        while start < end:  # only iterates through given indices
            output_list.append(input_list[start])
            start += 1

    return output_list


def add_at_index(list1: list[int], num: int, index: int) -> None:
    placeholder: list[int] = []  # empty list
    count: int = 0
    index_static: int = index  # stores another instance of index
    if index < 0 or index > len(list1):  # raises IndexError if invalid index is given
        raise IndexError("Index is out of bounds for the input list")

    for i in range(index):  # appends items from list1 into placeholder into given index
        placeholder.append(list1[i])

    placeholder.append(num)  # appends given number

    while index < len(list1):  # appends rest of list1 to placeholder
        placeholder.append(list1[index])
        index += 1

    while count < len(placeholder):  # copies placeholder over to list1
        if count > len(list1):
            list1.append(placeholder[count])
        if count == index_static:
            list1.append(num)
        list1[count] = placeholder[count]
        count += 1
