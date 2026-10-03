"""Running sums, constant-time range queries, and subarray counts."""

from collections.abc import Iterable


def running_sum(values: Iterable[int]) -> list[int]:
    """Return cumulative sums in O(n) time and O(n) output space."""
    result = []
    total = 0
    for value in values:
        total += value
        result.append(total)
    return result


class PrefixSums:
    """Snapshot integer values in O(n) time/space for O(1) range queries."""

    def __init__(self, values: Iterable[int]):
        self._prefix = [0]
        for value in values:
            self._prefix.append(self._prefix[-1] + value)

    def __len__(self) -> int:
        return len(self._prefix) - 1

    def range_sum(self, start: int, stop: int) -> int:
        """Sum the half-open interval [start, stop), like values[start:stop].

        Unlike slicing, invalid bounds raise IndexError rather than clipping.
        Empty ranges are valid, including [0, 0) on an empty input.
        """
        if not 0 <= start <= stop <= len(self):
            raise IndexError("expected 0 <= start <= stop <= number of values")
        return self._prefix[stop] - self._prefix[start]


def count_subarrays_with_sum(values: Iterable[int], target: int) -> int:
    """Count nonempty contiguous subarrays with the target sum.

    Supports negative numbers and zero. Expected O(n) time, O(n) extra space.
    Repeated prefix sums represent different possible starting positions.
    """
    frequencies = {0: 1}
    total = count = 0
    for value in values:
        total += value
        count += frequencies.get(total - target, 0)
        frequencies[total] = frequencies.get(total, 0) + 1
    return count


def longest_zero_sum_subarray(values: Iterable[int]) -> int:
    """Return the maximum zero-sum length; 0 if absent.

    Store only the first position for each prefix sum, giving the longest
    possible interval. Expected O(n) time and O(n) extra space.
    """
    first_seen = {0: -1}
    total = longest = 0
    for index, value in enumerate(values):
        total += value
        if total in first_seen:
            longest = max(longest, index - first_seen[total])
        else:
            first_seen[total] = index
    return longest
