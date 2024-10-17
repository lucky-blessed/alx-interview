# 0x0A. Prime Game

## Description
This project involves determining the winner of a competitive game between two players, Maria and Ben. The game is based on prime numbers and optimal play. Maria and Ben take turns selecting a prime number from a set of consecutive integers and removing that number along with its multiples from the set. The player who cannot make a move loses the game. The goal is to determine who wins the most rounds.

## Concepts Required
1. **Prime Numbers**:
   - Understanding prime numbers and efficient methods to identify primes.
   
2. **Sieve of Eratosthenes**:
   - Use the Sieve of Eratosthenes to efficiently find all primes up to any given limit.

3. **Game Theory**:
   - Apply basic game theory strategies to simulate optimal play for both players.

4. **Dynamic Programming/Memoization**:
   - Optimize the game state by caching results for repeated calculations across rounds.

5. **Python Programming**:
   - Use Python for implementing the game logic and prime number algorithms.

## Learning Objectives
- Efficiently generate prime numbers within a range.
- Simulate a game based on prime numbers and optimal moves.
- Use dynamic programming to store and reuse results.
- Write clean and efficient Python code adhering to the PEP 8 style guide.

## Requirements
- All files will be compiled/interpreted on **Ubuntu 20.04 LTS** using **python3 (version 3.4.3)**.
- Your code should follow the **PEP 8 style** (version 1.7.x).
- All your files should be executable and end with a new line.
- You must include a `README.md` file in the root of the project folder.
- You cannot import any external Python libraries or packages.
- The first line of all Python scripts must be `#!/usr/bin/python3`.

## Tasks

### 0. Prime Game
**Mandatory**

Maria and Ben play a game over `x` rounds. For each round `n` (where `n` is a number of consecutive integers starting from 1), they take turns choosing a prime number and removing that number along with its multiples. The player who cannot make a move loses the game.

- **Prototype**: `def isWinner(x, nums)`
- **Parameters**:
  - `x`: the number of rounds.
  - `nums`: an array containing `n` values for each round.
- **Returns**: the name of the player that won the most rounds. Return `None` if no winner can be determined.
  
Example:
```python
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: "Ben"

