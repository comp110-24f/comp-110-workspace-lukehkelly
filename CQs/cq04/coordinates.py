"""Coordinates file for CQ04"""

__author__ = "730761531"


def get_coords(xs: str, ys: str) -> None:
    outer_count: int = 0  # Count variables to iterate through
    inner_count: int = 0  # both while loops
    pair: str = ""  # empty string that will be concatenated

    while outer_count < len(xs):  # Outer while loop iterates through xs
        pair = "(" + xs[outer_count] + ","  # Concatenates first half of coordinate
        while inner_count < len(ys):  # Inner loop iterates through ys
            pair = (
                pair + ys[inner_count] + ")"
            )  # Concatenates second half of coordinate
            inner_count += 1  # Increases inner index
            print(pair)  # Prints coordinate
            pair = "(" + xs[outer_count] + ","  # resets string to the first half
        outer_count += 1  # Increases outer index
        inner_count = 0  # resests inner index so it will run through inner loop again


if __name__ == "__main__":
    get_coords(xs="12", ys="34")
    get_coords(xs="hi", ys="bye")
