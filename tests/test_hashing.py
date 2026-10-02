from collections import Counter
import itertools
import unittest

from algorithms.hashing import (
    contains_duplicate, first_unique_index, frequencies, two_sum_indices,
)


class HashingTests(unittest.TestCase):
    def test_frequencies_support_iterators_and_preserve_appearance_order(self):
        self.assertEqual(frequencies(iter("banana")), dict(Counter("banana")))
        self.assertEqual(list(frequencies("banana")), ["b", "a", "n"])
        self.assertEqual(frequencies([]), {})

    def test_first_unique_and_missing(self):
        self.assertEqual(first_unique_index(iter("aabbcd")), 4)
        self.assertEqual(first_unique_index("banana"), 0)
        self.assertIsNone(first_unique_index("aabb"))
        self.assertIsNone(first_unique_index([]))
        self.assertEqual(first_unique_index([None, "x", "x"]), 0)

    def test_duplicate_detection(self):
        self.assertTrue(contains_duplicate([1, 2, 1]))
        self.assertFalse(contains_duplicate([1, 2, 3]))
        self.assertFalse(contains_duplicate([]))

    def test_pair_uses_two_distinct_indices(self):
        self.assertIsNone(two_sum_indices([3], 6))
        self.assertEqual(two_sum_indices([3, 3], 6), (0, 1))
        self.assertEqual(two_sum_indices([2, 2, 7], 9), (0, 2))
        self.assertEqual(two_sum_indices([-3, 5, 2], -1), (0, 2))

    def test_pair_selection_against_brute_force(self):
        for length in range(5):
            for values in itertools.product([-1, 0, 1], repeat=length):
                for target in range(-2, 3):
                    expected = next(((i, j) for j in range(length) for i in range(j)
                                     if values[i] + values[j] == target), None)
                    self.assertEqual(two_sum_indices(iter(values), target), expected)


if __name__ == "__main__":
    unittest.main()
