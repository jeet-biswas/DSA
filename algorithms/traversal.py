"""Single-pass array problems. These functions never change their input."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def linear_search(values: Sequence[T], target: T) -> int:
    """Return the first matching index, or -1. O(n) time, O(1) extra space."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def min_max(values: Sequence[int]) -> tuple[int, int]:
    """Return (minimum, maximum). O(n) time, O(1) extra space.

    Raise ValueError for an empty sequence: there is no minimum or maximum.
    """
    if not values:
        raise ValueError("min_max requires at least one value")
    smallest = largest = values[0]
    for value in values:
        smallest = min(smallest, value)
        largest = max(largest, value)
    return smallest, largest


def second_largest(values: Sequence[int]) -> int | None:
    """Return the second DISTINCT largest value, or None if it does not exist.

    Keep the two largest distinct values seen so far. O(n) time, O(1) space.
    """
    largest = runner_up = None
    for value in values:
        if largest is None or value > largest:
            runner_up, largest = largest, value
        elif value != largest and (runner_up is None or value > runner_up):
            runner_up = value
    return runner_up
