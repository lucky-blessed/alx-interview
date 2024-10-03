# 0x08. Making Change

## Description

This project tackles the "coin change" problem, a classic algorithmic challenge. Given a list of coin denominations and a target total, the goal is to find the fewest number of coins needed to meet that total. The project explores both **Greedy Algorithms** and **Dynamic Programming** approaches to solve the problem efficiently.

## Learning Objectives

- Understand how **Greedy Algorithms** work and their limitations for the coin change problem.
- Apply **Dynamic Programming (DP)** to systematically solve the coin change problem for all possible totals.
- Analyze the time and space complexity of both greedy and DP algorithms.
- Improve **problem-solving strategies** by breaking down complex problems into smaller, manageable subproblems.
- Practice **Python programming** concepts such as lists, loops, and conditional statements.

## Requirements

- **Allowed editors**: `vi`, `vim`, `emacs`
- All code will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3 (version 3.4.3)**.
- All files should end with a new line.
- The first line of all Python files should be `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder, is mandatory.
- Code must follow **PEP 8 style** (version 1.7.x).
- All files must be **executable**.

## Tasks

### 0. Change Comes from Within

**Task:**  
Write a Python function that determines the fewest number of coins needed to meet a given total.

- **Prototype**: `def makeChange(coins, total)`
- **Parameters**:
  - `coins`: a list of integers representing the coin denominations.
  - `total`: an integer representing the amount to reach.
- **Return**:
  - The fewest number of coins needed to meet the total.
  - If the total is `0` or less, return `0`.
  - If the total cannot be met with the available coins, return `-1`.
  
**Example:**

```python
makeChange([1, 2, 5], 11)  # Returns: 3 (5 + 5 + 1)
makeChange([2], 3)         # Returns: -1 (impossible to make 3 with only coin denomination 2)

