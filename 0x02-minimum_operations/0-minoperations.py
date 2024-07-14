#!usr/bin/python3
"""
The module Minimum Operations
"""

def minOperations(n):
    """
    Calculates the minimum number of operations to achieve n characters (H).
    """
    if not isinstance(n, int) or n <= 1:
        return (0)

    operations = 0
    buffer_size = 0
    current_size = 1

    while current_size < n:
        if buffer_size == 0:
            buffer_size = current_size
            current_size += buffer_size
            operations += 2
        elif (n - current_size) % current_size == 0:
            buffer_size = current_size
            current_size += buffer_size
            operations += 2
        else:
            current_size += buffer_size
            operations += 1

    return operations          
