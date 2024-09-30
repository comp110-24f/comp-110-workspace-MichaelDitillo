"""CQ 4 Coordinates"""

__author__ = "730660760"


def get_coords(xs: str, ys: str) -> None:
    index_xs = 0  # indexes from 0
    while index_xs < len(xs):
        # continues indexing as long until all of xs has been exhausted
        index_ys = 0  # indexes from 0
        while index_ys < len(ys):
            # continues indexing as long until all of ys has been exhausted
            print("(" + xs[index_xs] + ", " + ys[index_ys] + ")")
            index_ys += 1  # indexes by one
        index_xs += 1  # indexes by one


# The code works by first making sure we are in xs
# the code then does the same thing for ys
# so it continues printing the ys, for the first xs, until all the possible ys
# are exhauseted
# then the code indexes by one to the next xs, and does the same
# repeating this process untill all the combinations of xs and ys have been
# exhausted
