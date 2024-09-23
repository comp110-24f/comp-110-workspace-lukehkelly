"""EX02 - Chardle - A cute step towards Wordle"""

__author__ = "730761531"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")

    if len(word) != 5:  # Checks if word is correct length
        print("Error: Word must contain 5 characters.")
        exit()  # Ends program if input is incorrect
    print(word)
    return word


def input_character() -> str:
    letter: str = input("Enter a single character: ")

    if len(letter) != 1:  # Checks if letter is a single character
        print("Error: Character must be a single character.")
        exit()  # Ends program if input is incorrect
    print(letter)
    return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)

    # If statements to check each index for letter
    if word[0] == letter:
        print(letter + " found at index 0")
    if word[1] == letter:
        print(letter + " found at index 1")
    if word[2] == letter:
        print(letter + " found at index 2")
    if word[3] == letter:
        print(letter + " found at index 3")
    if word[4] == letter:
        print(letter + " found at index 4")


def main() -> None:
    # Centralizes the code into one function
    contains_char(word=input_word(), letter=input_character())


if __name__ == "__main__":
    main()
