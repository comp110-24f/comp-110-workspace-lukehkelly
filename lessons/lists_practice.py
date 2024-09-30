"""Lists practice"""

my_numbers: list[float] = []

my_numbers.append(1.5)

game_points: list[int] = [102, 86, 94]

game_points[1] = 72

game_points.pop(1)


def display(set: list[int]) -> None:
    count = 0
    while count < len(set):
        print(set[count])
        count += 1


display(game_points)
