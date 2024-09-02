#!/usr/bin/python3
"""
Module to calculate the perimeter of n=an island in a grid.
"""


def island_perimeter(grid):
    """
    Returs the perimeter of the island described in the grid


    Args:
        grid (list of list of int): A rectangular grid where
        0 represents water and 1 represents land.


    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

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
