#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(n):
    """Generate a list of prime up to n using the sieve of erastosthenes"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def prime_counts(n, sieve):
    """Calculate the number of primes up to n"""
    return sum(sieve[:n + 1])


def isWinner(x, nums):
    """etermine the winner of each rounds"""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    sieve = sieve_of_eratosthenes(max_n)
    prime_win_counts = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_win_counts[i] = prime_win_counts[i - 1]
        if prime_counts(i, sieve) % 2 != 0:
            prime_win_counts[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_win_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
