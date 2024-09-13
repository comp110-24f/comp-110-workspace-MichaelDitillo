"""_MichaelDitillo_TeaParty_Excercise"""

__author__: str = "730660760"


def main_planner(guests: int) -> None:
    """entrypoint_of_function"""
    # takes inputed integer value, and takes this value as #number of guests

    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Adds required text and adds #guests as a str

    print("Tea Bags: " + str(tea_bags(people=guests)))
    # prints required text and calls tea bags by setting people=guests,
    # return corresponding teas as a string added totext

    print("Treats: " + str(treats(people=guests)))
    # prints required text and calls treats by setting people=guests,
    # return correpsonding treast as a string added to text

    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# prints required text, and adds the result of a cost function as a str to the text
# within the call of the cost function, tea_count, treat_count functions are called
# this way cost corresponds to the number of teas and treats


def tea_bags(people: int) -> int:
    """Returns number of Tea bags"""
    return people * 2
    # multiplies the number of people by 2 to get 2 teabags per person


def treats(people: int) -> int:
    """Finds the number of treats needed for a number of people"""
    return int(tea_bags(people=people) * 1.5)
    # takes the number of people multiplies by 1.5 to get req treats
    # then converts float value to an int, so the function can executre


def cost(tea_count: int, treat_count: int) -> float:
    """Cost_of_Tea_and_treats_combined"""
    return tea_count * 0.5 + treat_count * 0.75
    # takes tea count and multiplies by 0.5, takes treat count and multiples by 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # when program is ran this spits out the above question
    # allows, for a number of guests to be inputed
