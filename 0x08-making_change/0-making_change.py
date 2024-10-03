#!/usr/bin/python3
"""
This module provides a function makeChanges to determine
the minimum number of coins needed to make a
given amount of change

Concepts:
	- Greedy Algorithm
	- Dynamic programming
	- Algorithic complecity
"""

def makeChange(coins, total):
    """
    To determine the fewest number of coins needed to make
    a given totaly.

    Args:
        coins (list of in): A list of the of the value of cons
        in your possession where each vaue us an integer 
        greater than zero (0).
        total (int): The total amount to achieve with the
        fewest number of coins.

    Returns:
        int: Fewest number of coins needed to make a total.
        - if the total is 0 or less, return 0
        - if the total connot be met by any combination of
          coins, return -1
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for k in range(coin, total + 1):
            dp[k] = min(dp[k], dp[k - coin] + 1)

        return dp[total] if dp[total] != float('inf') else -1
