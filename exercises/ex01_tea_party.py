"""_MichaelDitillo_TeaParty_Excercise"""

__author__: str = "730660760"


def main_planner(guests: int) -> None:
    """entrypoint_of_function"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    """Adds_required_text_and_takes_and_inputs_#guests_as_a_str"""

    print("Tea Bags: " + str(tea_bags(people=guests)))
    """adds_required_text_and_calls_tea_bags_by_setting_guests=people"""

    print("Treats: " + str(treats(people=guests)))
    """does_the_same_as_last_print_for_treats"""

    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


"""returns_total_cost_by_assigning_count_values_to_the_#teas_and_#treats"""


def tea_bags(people: int) -> int:
    """Returns_number_of_Tea_bags_2"""
    return people * 2


def treats(people: int) -> int:
    """muliplies_tea_bags_by_1.5_and_converts_float_to_int_before_returning_=#treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost_of_Tea_and_treats_combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
