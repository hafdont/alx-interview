#!/usr/bin/python3
"""
This modulescontains minOperations function.
"""

def minOperations(n);
    """
    Calculates the minimum number of operations to achieve n characters (H).

    Args:
        n: The target number of characters

    Returns:
        The minimum number of operations needed, or 0 if impossible.
    """

    if n <= 1:
        return 0


    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
