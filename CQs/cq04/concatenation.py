"""Concatenation file for CQ04"""

__author__ = "730761531"


def concat(var1: str, var2: str) -> str:
    return var1 + var2


word1: str = "happy"
word2: str = "tuesday"


if __name__ == "__main__":
    print(concat(var1=word1, var2=word2))
