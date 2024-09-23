"""Practice with conditionals"""

"""
def check_first_letter(word: str, letter: str) -> str:

    if word[0] == letter:
        return "Match!"
    else:
        return "No match!"
"""

# print(check_first_letter(word="happy", letter="h"))


def get_weather_report() -> str:
    weather: str = input("What is the weather? ")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
