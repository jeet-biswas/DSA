import bisect
import itertools
import unittest

from algorithms.binary_search import (
    binary_search, count_occurrences, lower_bound, upper_bound,
)


class BinarySearchTests(unittest.TestCase):
    def test_empty_and_boundary_matches(self):
        self.assertEqual(binary_search([], 1), -1)
        self.assertEqual(lower_bound([], 1), 0)
        self.assertEqual(upper_bound([], 1), 0)
        self.assertEqual(binary_search([2, 4, 6], 2), 0)
        self.assertEqual(binary_search([2, 4, 6], 6), 2)
        self.assertEqual(binary_search([2, 4, 6], 5), -1)

    def test_duplicate_bounds(self):
        values = [1, 2, 2, 2, 9]
        self.assertEqual(binary_search(values, 2), 1)
        self.assertEqual(lower_bound(values, 2), 1)
        self.assertEqual(upper_bound(values, 2), 4)
        self.assertEqual(count_occurrences(values, 2), 3)

    def test_exhaustive_small_sorted_sequences_against_standard_library(self):
        for length in range(6):
            for values in itertools.combinations_with_replacement(range(-2, 3), length):
                for target in range(-3, 4):
                    with self.subTest(values=values, target=target):
                        self.assertEqual(lower_bound(values, target), bisect.bisect_left(values, target))
                        self.assertEqual(upper_bound(values, target), bisect.bisect_right(values, target))
                        self.assertEqual(count_occurrences(values, target), values.count(target))
                        expected = values.index(target) if target in values else -1
                        self.assertEqual(binary_search(values, target), expected)


if __name__ == "__main__":
    unittest.main()
