#!/usr/bin/python3
"""Module for calculating rainwater retention between walls."""


def rain(walls):
    """Calculate the total amount of rainwater retained between walls.

    Args:
        walls (list): A list of non-negative integers representing wall heights.

    Returns:
        int: Total square units of rainwater retained. Returns 0 if list is empty.
    """
    if not walls:
        return 0

    n = len(walls)
    total = 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    for i in range(n):
        water = min(left_max[i], right_max[i]) - walls[i]
        if water > 0:
            total += water

    return total
    