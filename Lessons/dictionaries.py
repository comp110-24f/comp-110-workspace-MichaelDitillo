"""Learning Dictionaries Lesson 18"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["vanilla"] += 110
# changes the value of vanilla from 8 to 118, 8 + 110

print(len(ice_cream))
# prints 3

ice_cream["mint"] = 3
# add key-value entry by directly assigning to a key

has_pbj: bool = "pbj" in ice_cream
# test if "pbj" is a key in ice_cream

print(ice_cream["chocolate"])
# Prints 12

ice_soda: dict[str, str] = {"cheese": "cheese"}
# Shows you can have a dictionary with key and value defined by the same data type

ice_cream.pop("strawberry")
# to remove, we use the pop method and dive a key
# if you were to print the above line of code it would return 4

for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")
# to iterate over every key in a loop, use for loop
