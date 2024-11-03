"""EX06 - Dictionary Utils"""

__author__ = "730761531"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    output: dict[str, str] = {}  # empty dict

    for key in input_dict:
        if (
            input_dict[key] in output
        ):  # checks if input_dict value occurs as a key in output
            raise KeyError("No duplicates allowed")
        output[(input_dict[key])] = key  # inverts the dictionary

    return output


def favorite_color(input_dict: dict[str, str]) -> str:
    result: dict[str, int] = {}  # empty dict to track color-occurences
    maxi: int = 0  # tracks color w most occurences
    current_most: str = ""  # tracks string literal of most occurences

    for key in input_dict:  # Adds color-occurence key-values to empty dict
        if key in result:
            result[key] += 1
        else:
            result[key] = 1

    for key in result:
        if result[key] > maxi:  # checks if occurences is greater than maxi
            current_most = input_dict[key]  # reassigns current_most to new string
            maxi = result[key]  # maxi reassigned to int of most occurences

    return current_most


def count(input_list: list[str]) -> dict[str, int]:
    output: dict[str, int] = {}

    for item in input_list:
        if item in output:  # if item already occurs, increment by 1
            output[item] += 1
        else:  # if doesn't exist yet, initiliaze new key-value with value of 1
            output[item] = 1
    return output


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    output: dict[str, list[str]] = {}

    for item in input_list:  # create a key for each occuring letter
        output[item.lower()[0]] = []

    for item in input_list:  # if item starts with key, add it to that key's list
        if item.lower()[0] in output:
            output[item.lower()[0]].append(item)

    return output


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:

    if day in input_dict:  # checks if day alr exists
        input_dict[day].append(student)  # adds student to that day's list
    else:
        input_dict[day] = [student]  # creates a new day containing that student
    return
