#!/usr/bin/python3
"""
This moduke provides a function makeChange to determine the
minimum number of coins needed to make a given
amount of change


Concepts:
    - Greedy Algorithm
    - Dynamwic Programming
    - Algorithmic complexity
"""


def makeChange(coins, total):
    """
    To determine the fewsest number of coins needed to make
    a given total.

    Args:
        coins (list of int): A list of the values of coins
        in your possesion where each value is an interger
        greater than 0
        total (int): The total amount to achieve with the
        fewest number of coins


    Returns:
        int: Fewest number of coins needed to make a total
             If the total is 0 or less, return 0
             If the totla connnot be met by any combination
             of coins, return -1
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for k in range(coin, total + 1):
            dp[k] = min(dp[k], dp[k - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
