"""Frequency and membership problems using hash tables.

Dictionary/set operations are expected O(1); unusual hash collisions can make
them slower. Input values must be hashable. Inputs are never modified.
"""

from collections.abc import Hashable, Iterable
from typing import TypeVar

T = TypeVar("T", bound=Hashable)


def frequencies(values: Iterable[T]) -> dict[T, int]:
    """Count values in first-appearance order. Expected O(n) time/O(u) space."""
    counts: dict[T, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


def first_unique_index(values: Iterable[T]) -> int | None:
    """Index of the first value appearing once; None if absent.

    Track counts and first positions to support a one-shot iterable without
    copying it. Expected O(n) time and O(u) space for u distinct values.
    """
    counts: dict[T, int] = {}
    first_positions: dict[T, int] = {}
    for index, value in enumerate(values):
        counts[value] = counts.get(value, 0) + 1
        first_positions.setdefault(value, index)
    for value, position in first_positions.items():
        if counts[value] == 1:
            return position
    return None


def contains_duplicate(values: Iterable[T]) -> bool:
    """Check for a repeated value. Expected O(n) time and O(u) space."""
    seen: set[T] = set()
    for value in values:
        if value in seen:
            return True
        seen.add(value)
    return False


def two_sum_indices(values: Iterable[int], target: int) -> tuple[int, int] | None:
    """Return distinct indices (i, j), i < j, whose values sum to target.

    Choose the earliest finishing pair, keeping the first index of each value.
    No sorting is needed. Expected O(n) time and O(n) space.
    """
    first_seen: dict[int, int] = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in first_seen:
            return first_seen[complement], index
        first_seen.setdefault(value, index)
    return None
