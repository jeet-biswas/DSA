"""Opposite-direction pointer patterns adapted from the original notebook."""

from collections.abc import MutableSequence, Sequence
from typing import TypeVar

T = TypeVar("T")


def reverse_in_place(values: MutableSequence[T]) -> None:
    """Reverse a mutable sequence. O(n) time, O(1) extra space."""
    left, right = 0, len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1


def is_palindrome(values: Sequence[T]) -> bool:
    """Check exact equality from both ends. O(n) time, O(1) extra space.

    Empty and singleton sequences are palindromes. Strings are case-sensitive
    and punctuation is not stripped.
    """
    left, right = 0, len(values) - 1
    while left < right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1
    return True


def unique_pairs(values: Sequence[int], target: int) -> list[tuple[int, int]]:
    """Return distinct VALUE pairs summing to target from an ascending input.

    The input must already be sorted. A pair uses two different positions, so
    (2, 2) needs two 2s. O(n) time and O(p) output space for p pairs.
    """
    pairs = []
    left, right = 0, len(values) - 1
    while left < right:
        total = values[left] + values[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            low, high = values[left], values[right]
            pairs.append((low, high))
            while left < right and values[left] == low:
                left += 1
            while left < right and values[right] == high:
                right -= 1
    return pairs


def max_container_area(heights: Sequence[int]) -> int:
    """Largest area between nonnegative heights at unit-spaced positions.

    Move the shorter wall: narrowing the width while keeping that wall cannot
    improve the area. O(n) time, O(1) extra space. Return 0 for fewer than two
    walls. Negative heights raise ValueError.
    """
    if any(height < 0 for height in heights):
        raise ValueError("heights must be nonnegative")
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(heights[left], heights[right]))
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return best
