#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
    grid (list of int): 2D grid where 0 represents water and
    1 represent land.

    Returns:
    int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
