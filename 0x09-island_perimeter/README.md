# 0x09. Island Perimeter

## Description

The **Island Perimeter** project involves solving a geometric problem within a grid context. The task is to calculate the perimeter of a single island in a grid, where the grid is represented as a 2D array of integers. Each element in the grid can be either water (`0`) or land (`1`). The objective is to develop a function that calculates the perimeter of the island, ensuring correct counting of all edges that contribute to the perimeter.

### Key Concepts

- **2D Arrays (Matrices)**: 
  - Working with 2D lists (grids) in Python.
  - Accessing and iterating over elements in a 2D array.
  - Understanding how to navigate adjacent cells in the grid (up, down, left, right).
  
- **Conditional Logic**:
  - Applying conditions to determine whether a cell contributes to the perimeter.
  
- **Counting Techniques**:
  - Efficiently counting the perimeter contributions from each land cell.
  
- **Problem-Solving**:
  - Breaking down the problem into smaller sub-tasks such as identifying land cells, checking neighbors, and calculating contributions.

## Requirements

- **Python version**: `3.4.3`
- **Operating system**: Ubuntu 20.04 LTS
- No additional modules or imports allowed.
- Code must follow the **PEP 8** style guide.
- Files should end with a new line.
- All files must be executable and start with a shebang (`#!/usr/bin/python3`).

## Files

### `0-island_perimeter.py`

This file contains the solution to the island perimeter problem. The function `island_perimeter(grid)` takes a 2D grid of integers as input and returns an integer representing the total perimeter of the island.

- **Prototype**: `def island_perimeter(grid):`
- **Input**:
  - `grid` is a list of lists of integers, where:
    - `0` represents water.
    - `1` represents land.
  - Each cell is a square with side length `1`.
  - Cells are connected horizontally or vertically, but not diagonally.
  - The grid is rectangular with dimensions not exceeding 100.
  - The grid is completely surrounded by water.
  - There is exactly one island (or no island), with no lakes (water within the island that isn't connected to the surrounding water).

### Example:

```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16

