"""Run from the repository root: python -m examples.practice_demo."""

from algorithms.binary_search import binary_search, count_occurrences
from algorithms.hashing import frequencies, two_sum_indices
from algorithms.prefix_sum import PrefixSums, count_subarrays_with_sum
from algorithms.sliding_window import longest_distinct_window, max_window_sum
from algorithms.sorting import insertion_sort, merge_sort
from algorithms.stacks_queues import TwoStackQueue, brackets_balanced, next_greater_values
from algorithms.traversal import min_max, second_largest
from algorithms.two_pointers import max_container_area, unique_pairs


def main() -> None:
    print("Traversal:", min_max([4, -2, 9]), second_largest([9, 9, 4]))
    print("Binary search:", binary_search([1, 2, 2, 4], 2),
          "occurrences:", count_occurrences([1, 2, 2, 4], 2))
    print("Range [1, 4):", PrefixSums([6, 3, 8, 2, 5]).range_sum(1, 4))
    print("Zero-sum subarray count:", count_subarrays_with_sum([1, -1, 0], 0))
    print("Frequencies:", frequencies("banana"))
    print("Unsorted two-sum indices:", two_sum_indices([7, 2, 11, 15], 9))
    print("Sorted unique pairs:", unique_pairs([1, 1, 2, 3, 4, 4], 5))
    print("Container area:", max_container_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print("Best width-2 sum:", max_window_sum([2, -1, 4, 3], 2))
    print("Longest distinct window:", longest_distinct_window("abba"))
    print("Balanced brackets:", brackets_balanced("{a + (b * [c])}"))
    print("Next greater values:", next_greater_values([2, 1, 3]))
    queue: TwoStackQueue[str] = TwoStackQueue()
    queue.enqueue("first")
    queue.enqueue("second")
    print("FIFO order:", queue.dequeue(), queue.dequeue())
    print("Insertion sort:", insertion_sort([3, -1, 2, 3]))
    print("Merge sort:", merge_sort([3, -1, 2, 3]))


if __name__ == "__main__":
    main()
