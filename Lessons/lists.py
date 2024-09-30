"""Basic Lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

my_numbers.append(1.5)
my_numbers.append(2.3)
# print(my_numbers)

# str analogy
# my_name: str = "" # literal
# ny_name: stri = str() #constructor

# creating an already populated list
game_points: list[int] = [102, 86, 94]
# print(game_points)

# prints third value of game points list
# print(game_points[2])

# prints last value of game_points
# print(game_points[len(game_points) - 1])

# Modifying by Index
# changes second value in game_points to 72
# lists are mutable
game_points[1] = 72
print(game_points)

# shows what happens when you attempt to index a value outside the list
# print(game_points[3])

# shows how you can modify lists, by individual objeects, but cannot for str
# class_num: str = "110"  # Change it to ";
# class_num[0] = "2"

# Removing items from a list
game_points.pop(1)
print(game_points)

# Repeating items
# shows you can add a value already in the list
game_points.append(94)
print(game_points)


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
