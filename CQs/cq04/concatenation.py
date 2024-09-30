"""CQ 4 Concatenation"""

__author__ = "730660760"


def concat(str_1: str, str_2: str) -> str:
    """Concatintates strings"""
    return str_1 + str_2


# combines strings

word1 = "happy"
word2 = "tuesday"

# defines the global variables word1 and word2


if __name__ == "__main__":
    print(concat(word1, word2))

# ensures the concat function is only executed within this module
# before the print and subsquent calling of concat is evaluated
