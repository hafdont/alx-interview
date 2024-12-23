#!/usr/bin/python3
"""
Make module
"""


def makeChange(coins, total):
    """
    finds the fewest coins required to meet total 
    given a pile of coins different amounts
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
