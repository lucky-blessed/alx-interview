#!/usr/bin/python3
"""
Prime Game
"""


def sieve_of_eratosthenes(n):
    """
    Returns a list of prime up to n using the sieve
    of Eratosthenes.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        primes_up_to_n = [i for i in range(2, n + 1) if primes[i]]
        if not primes_up_to_n:
            wins['Ben'] += 1
            continue

        move_count = 0
        removed = [False] * (n + 1)

        for prime in primes_up_to_n:
            if not removed[prime]:
                move_count += 1
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
        if move_count % 2 == 1:
            wins['Maria'] += 1
        else:
            wins['Ben'] += 1
    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None
