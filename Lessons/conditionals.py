"""Practice with conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if num is <10"""
    dub: int = num * 2
    print(dub)
    if num < 10:
        print("Small Number!")
    else:
        print("Big Number!")
    print("Have a nice day!")


def should_i_eat(hungry: bool) -> None:
    "Tells me whether or not to eat based on hunger"
    if hungry:
        print("Eat some food silly goose!")
    else:
        print("Do your comp Hw")
    print("I am proud of you")


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match"
    else:
        return "no match"


print(check_first_letter(word="happy", letter="h"))
