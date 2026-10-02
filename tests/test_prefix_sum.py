import itertools
import unittest

from algorithms.prefix_sum import (
    PrefixSums, count_subarrays_with_sum, longest_zero_sum_subarray, running_sum,
)


class PrefixSumTests(unittest.TestCase):
    def test_running_sum_and_iterators(self):
        self.assertEqual(running_sum([]), [])
        self.assertEqual(running_sum(iter([5, 2, -8, 3])), [5, 7, -1, 2])

    def test_all_valid_ranges_and_source_mutation(self):
        values = [6, 3, 8, -2, 5, 4, 6]
        prefix = PrefixSums(values)
        for start in range(len(values) + 1):
            for stop in range(start, len(values) + 1):
                self.assertEqual(prefix.range_sum(start, stop), sum(values[start:stop]))
        original_sum = sum(values)
        values[0] = 100
        self.assertEqual(prefix.range_sum(0, len(prefix)), original_sum)
        self.assertEqual(PrefixSums([]).range_sum(0, 0), 0)

    def test_invalid_ranges(self):
        prefix = PrefixSums([1, 2, 3])
        for start, stop in [(-1, 2), (2, 1), (0, 4), (4, 4)]:
            with self.subTest(start=start, stop=stop), self.assertRaises(IndexError):
                prefix.range_sum(start, stop)

    def test_repeated_zero_prefixes(self):
        self.assertEqual(count_subarrays_with_sum([0, 0, 0], 0), 6)
        self.assertEqual(longest_zero_sum_subarray([3, 4, -7, 2, -2]), 5)

    def test_small_sequences_against_brute_force(self):
        for length in range(5):
            for values in itertools.product([-1, 0, 1], repeat=length):
                ranges = [(sum(values[left:right]), right - left)
                          for left in range(length) for right in range(left + 1, length + 1)]
                for target in [-2, 0, 2]:
                    self.assertEqual(count_subarrays_with_sum(values, target),
                                     sum(total == target for total, _ in ranges))
                self.assertEqual(longest_zero_sum_subarray(values),
                                 max((size for total, size in ranges if total == 0), default=0))


if __name__ == "__main__":
    unittest.main()
