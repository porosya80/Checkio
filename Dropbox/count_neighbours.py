#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py check count-neighbours

# https://py.checkio.org/mission/count-neighbours/

# "Animals and plants can reproduce themselves,        but it was only recently shown that machines can be made which also        reproduce themselves... Other kinds of self-reproducing machines        will be described, and one simple mechanical        model, with no electrical or magnetic complications,        will be there in working order for the audience to inspect and operate."
#
# -- Edward Forrest Moore
#
# In cellular automata,the    Moore neighborhoodcomprises    the eight cells surrounding a central cell on a two-dimensional square lattice.    The neighborhood is named after Edward F. Moore, a pioneer of cellular automata theory.    Many board games are played with a rectangular grid with squares as cells.    For some games, it is important to know about the conditions of neighbouring cells for chip    (figure, draught etc) placement and strategy.
#
# You are given a state for a rectangular board game grid with chips in a binary matrix, where 1    is a cell with a chip and 0 is an empty cell. You are also given the coordinates for a cell in    the form of row and column numbers (starting from 0). You should determine how many chips are    close to this cell. Every cell interacts with its eight neighbours; those cells that are    horizontally, vertically, or diagonally adjacent.
#
#
#
# For the given examples (see the schema) there is the same grid:
#
#
# ((1, 0, 0, 1, 0),
#  (0, 1, 0, 0, 0),
#  (0, 0, 1, 0, 1),
#  (1, 0, 0, 0, 0),
#  (0, 0, 1, 0, 0),)
#
# For the first example coordinates of the cell is (1, 2) and    as we can see from the schema this    cell has 3 neighbour chips.    For the second example coordinates is (0, 0) and this cell contains    a chip, but we count only neighbours and the answer is 1.
#
# Input:Three arguments. A grid as a tuple of tuples with integers (1/0),    a row number and column number for a cell as integers.
#
# Output:How many neighbouring cells have chips as an integer.
#
#
# Precondition:
# 3 ≤ len(grid) ≤ 10
# all(len(grid[0]) == len(row) for row in grid)
#
#
# END_DESC


def in_bounds(grid, row, col):
    if row < 0 or col < 0:
        return False
    if row > len(grid)-1 or col > len(grid[0])-1:
        return False
    return True


def count_neighbours(grid, row, col):
    result = 0
    for y_offset in (-1, 0, 1):
        for x_offset in (-1, 0, 1):
            row_x = row+x_offset
            col_y = col+y_offset
            if not (row_x == row and col_y == col):
                if in_bounds(grid, row_x, col_y):
                    if grid[row_x][col_y] == 1:
                        result += 1

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
