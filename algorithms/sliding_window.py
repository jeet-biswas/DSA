"""Fixed-size and variable-size windows over contiguous input."""

from collections.abc import Hashable, Sequence
from typing import TypeVar

T = TypeVar("T", bound=Hashable)


def max_window_sum(values: Sequence[int], window_size: int) -> int:
    """Maximum sum of exactly window_size consecutive elements.

    O(n) time and O(1) extra space; handles all-negative inputs. Raise ValueError
    unless 1 <= window_size <= len(values). Input is never modified.
    """
    if not 1 <= window_size <= len(values):
        raise ValueError("window_size must be between 1 and the input length")
    current = sum(values[index] for index in range(window_size))
    best = current
    for right in range(window_size, len(values)):
        current += values[right] - values[right - window_size]
        best = max(best, current)
    return best


def longest_distinct_window(values: Sequence[T]) -> int:
    """Length of the longest contiguous window without repeated values.

    Move the left boundary past an in-window repeat, never backwards.
    Expected O(n) time and O(u) space for u distinct, hashable values.
    """
    last_seen: dict[T, int] = {}
    left = best = 0
    for right, value in enumerate(values):
        if value in last_seen:
            left = max(left, last_seen[value] + 1)
        last_seen[value] = right
        best = max(best, right - left + 1)
    return best
