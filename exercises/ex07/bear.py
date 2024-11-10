"""File to define Bear class."""

__author__ = "730660760"


class Bear:
    """This represents a bear in our simulation, it can age and get hungry."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Constructor for Bear."""
        self.age = 0
        self.hunger_score = 0
        return None
        # Initializes age and hunger from 0

    def one_day(self) -> None:
        """Ages Bears by one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
        # with each day, when the one_day method is called, age increases one and hunger
        # decreases one

    def eat(self, num_fish: int) -> None:
        """Defines when bears eat."""
        self.hunger_score += num_fish
        return None
        # the hunger score increases by the amount of fish the bear eats
