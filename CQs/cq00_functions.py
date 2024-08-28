"""First CQ - function practice"""

__author__ = "730761531"


def mimic(message: str) -> str:
    """Returns message variable"""

    return message


def main() -> None:
    """Calls and prints mimic function"""

    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
