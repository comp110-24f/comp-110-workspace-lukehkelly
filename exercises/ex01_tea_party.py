"""Plans a tea party using number of people, teabags, treats, and cost"""

__author__ = "730761531"


def main_planner(guests: int) -> None:
    """Brings all functions together and prints output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=tea_bags(people=guests), treat_count=treats(people=guests)
            )  # Nests arguments from tea_bags and treats that are necessary for cost
        )
    )


def tea_bags(people: int) -> int:
    """Multiplies people by 2 to determine number of teabags"""
    return people * 2  # Multiplies total people by 2


def treats(people: int) -> int:
    """Multiplies treats by teabags to get total number of treats needed"""
    return int(1.5 * tea_bags(people=people))  # Multiplies total teabags by 1.5


def cost(tea_count: int, treat_count: int) -> float:
    """Computes total cost of treats and teabags"""
    return (tea_count * 0.5) + (
        treat_count * 0.75
    )  # Tea bags cost 50 cent and treats cost 75 cent, so this multiplies total counts
    # of each and adds them together to get total cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
