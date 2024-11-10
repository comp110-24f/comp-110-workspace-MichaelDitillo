"""For Running EX07."""

__author__ = "730660760"

from exercises.ex07.river import River

my_river: River = River(num_fish=10, num_bears=2)


my_river.view_river()

# creates a new instance of type River

my_river.one_river_week()

# calls the method one_river_week
