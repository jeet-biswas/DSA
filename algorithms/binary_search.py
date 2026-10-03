"""Binary search on sequences already sorted in ascending order.

Sorting is the caller's responsibility. All functions take O(log n) time and
O(1) extra space, and leave the sequence unchanged.
"""

from collections.abc import Sequence


def lower_bound(values: Sequence[int], target: int) -> int:
    """First index with value >= target; len(values) if none exists."""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left


def upper_bound(values: Sequence[int], target: int) -> int:
    """First index with value > target; len(values) if none exists."""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] <= target:
            left = middle + 1
        else:
            right = middle
    return left


def binary_search(values: Sequence[int], target: int) -> int:
    """Return the first matching index, including with duplicates, or -1."""
    index = lower_bound(values, target)
    return index if index < len(values) and values[index] == target else -1


def count_occurrences(values: Sequence[int], target: int) -> int:
    """Count target occurrences without scanning the matching range."""
    return upper_bound(values, target) - lower_bound(values, target)
