"""Uses a while loop to iterate over a string"""

__author__ = "730761531"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
