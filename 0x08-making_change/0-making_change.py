#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for k in range(coin, total + 1):
            dp[k] = min(dp[k], dp[k - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
