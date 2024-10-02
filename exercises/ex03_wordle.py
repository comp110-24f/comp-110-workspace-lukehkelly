"""EX03 - Wordle"""

__author__ = "730761531"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_len: int) -> str:
    while True:  # While loop to ask for guess of same length as secret
        guess: str = input(f"Enter a {secret_word_len} character word: ")
        if len(guess) != secret_word_len:  # Makes sure lengths are equal
            print(f"That wasn't {secret_word_len} chars! Try again: ")
        else:
            return guess


def contains_char(searched_str: str, search_char: str) -> bool:
    """Returns True if search_char is found in searched_str"""
    assert len(search_char) == 1
    count: int = 0

    while count < len(
        searched_str
    ):  # While loop to search through searched_str and returns T/F if search_char is found
        if searched_str[count] == search_char:
            return True
        else:
            count += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Returns an emojified version of user_guess in relation to secret_word"""
    assert len(user_guess) == len(secret_word)
    count: int = 0
    output: str = ""

    while count < len(secret_word):
        if (
            user_guess[count] == secret_word[count]
        ):  # Appends a green box if letter is correct
            output += GREEN_BOX
            count += 1
        elif contains_char(searched_str=secret_word, search_char=user_guess[count]):
            output += YELLOW_BOX  # Utilizes contains_char function to determine
            count += 1  # if a yellow box should be appended
        else:  # If nothing is found, adds a white box
            output += WHITE_BOX
            count += 1

    return output


def main(secret: str) -> None:
    """Entrypoint of program and main game loop"""
    turn: int = 1
    won: bool = False
    guess: str = ""
    while (
        turn <= 6 and won == False
    ):  # Ensures that adequate turns are remaining and player hasn't won yet
        print(f"== Turn {turn}/6 ==")
        guess = input_guess(secret_word_len=len(secret))
        print(emojified(user_guess=guess, secret_word=secret))
        if guess == secret:  # Ends loop by changing won to True
            print(f"You won in {turn}/6 turns!")
            won = True
        else:  # If incorrect, increments turn by 1
            turn += 1
    if turn > 6:
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
