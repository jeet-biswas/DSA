"""Two stable sorting algorithms that return a new list.

These implementations are for learning. Python's built-in sorted() is the
usual choice for application code.
"""

from collections.abc import Iterable


def insertion_sort(values: Iterable[int]) -> list[int]:
    """Insert each value into the sorted prefix of a copied list.

    O(n**2) worst-case time, O(n) best-case time for already sorted input.
    O(n) space for the returned copy, O(1) working space beyond that copy.
    """
    result = list(values)
    for index in range(1, len(result)):
        value = result[index]
        position = index
        while position > 0 and result[position - 1] > value:
            result[position] = result[position - 1]
            position -= 1
        result[position] = value
    return result


def merge_sort(values: Iterable[int]) -> list[int]:
    """Sort by splitting and merging. O(n log n) time and O(n) extra space.

    Recursion depth is O(log n). Prefer the left half on ties to preserve the
    original order of equal values.
    """
    result = list(values)
    if len(result) < 2:
        return result
    middle = len(result) // 2
    left = merge_sort(result[:middle])
    right = merge_sort(result[middle:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
