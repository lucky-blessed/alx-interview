#!/usr/bin/python3
"""
Minimum Operation Module
"""


def minOperations(n):
    """
    To calculate the fewest number of operations needed to result in
    exactly n 'H' characters in the file.

    Args:
        n: The target number of H characters.


    Returns:
        The minimum number of operation needed, or 0 if n cannot be achieved
    """
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 1
        current_length += clipboard
        operations += 1

    return operations
