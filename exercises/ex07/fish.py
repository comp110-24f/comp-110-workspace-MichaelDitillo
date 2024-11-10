"""File to define Fish class."""

__author__ = "730660760"


class Fish:
    """Represents a Fish in our fish simulation, as time progresses the fish ages."""

    age: int

    def __init__(self) -> None:
        """Fish Constructor."""
        self.age = 0
        return None
        # Constructore for Fish, initializers age to 0

    def one_day(self) -> None:
        """Ages Fish by One."""
        self.age += 1
        return None
        # Fish age increases by one each time this method is called
