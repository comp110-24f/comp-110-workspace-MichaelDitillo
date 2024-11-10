"""File to define River class."""

__author__ = "730660760"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Brings together our fish and bear classes to create a simulation a river."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    # attributes, which relate the Fish class and Bear class into our River class
    # we now also have time as an attribute

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks Animal Ages."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        # creates two empty lists of type Fish and of type Bear
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        for bears in self.bears:
            if bears.age <= 5:
                surviving_bears.append(bears)
        # iterates over each of these lits, and appends the animals to the new list
        # if they meet the age criteria
        self.fish = surviving_fish
        self.bears = surviving_bears
        # fish and bears take on the values of the new lists
        return None

    def bears_eating(self) -> None:
        """When Bears Eat."""
        # Only let the bears eat if there are at least 5 fish
        while len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
            self.remove_fish(3)
        # if there are at leat 5 fish remaining, the bear eats a fish, and the
        # method remove_fish() is called removing 3 fishes, this continues, until
        # there are no longer at least 5 remaining
        return None

    def check_hunger(self) -> None:
        """Checks Hunger Level."""
        surviving_bears: list[Bear] = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                surviving_bears.append(bears)
        self.bears = surviving_bears
        return None

    # similar to the above check_ages() method only this time the criteria, is
    # having a non-negative level of hunger. The method works by creating and empty list
    # iterating over self.bears with a for loop and assining those bears with
    # a non-negative hunger to the new list, which is then reassigned back to
    # self.bears

    def repopulate_fish(self) -> None:
        """Repopulation of Fish."""
        for x in range(len(self.fish) // 2):
            # floor division operator, ensures the range of x, only includes
            # the number of pairs of fish
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            # for each pair of fish Fish() is called four times  instantiating 4 new
            # Fish as each pair of fish creats 4 new fish
        return None

    def repopulate_bears(self) -> None:
        """Repopulation of Bears."""
        for x in range(len(self.bears) // 2):
            self.bears.append(Bear())
        # floor division operator ensures only pairs of bears are in the range
        # for each a new Bear is instantiated
        return None

    def view_river(self) -> None:
        """Prints the Status of the River."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None
        # Uses 4 typing to print the above four messages tracking the health of the river

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulates one week in the River."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
        # As there are 7 days in a way, this method calls the method one_river_day
        # 7 times

    def remove_fish(self, amount: int) -> None:
        """Removes fish."""
        for i in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
        # Iterates over amount, while i is still in range of amount,
        # if the number of fish is positive, then the fish are removed
        # since the we are pop(0), the first index is removed each time the
        # loop evaluates
        return None
