import itertools
import unittest

from algorithms.two_pointers import (
    is_palindrome, max_container_area, reverse_in_place, unique_pairs,
)


class TwoPointerTests(unittest.TestCase):
    def test_reverse_changes_same_list(self):
        for values in [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]:
            expected = values[::-1]
            self.assertIsNone(reverse_in_place(values))
            self.assertEqual(values, expected)

    def test_palindrome_semantics(self):
        for values in [[], [1], [1, 2, 1], "", "level"]:
            self.assertTrue(is_palindrome(values))
        self.assertFalse(is_palindrome("Level"))
        self.assertFalse(is_palindrome([1, 2]))

    def test_unique_pairs_with_duplicates(self):
        self.assertEqual(unique_pairs([1, 1, 1, 4, 4, 4], 5), [(1, 4)])
        self.assertEqual(unique_pairs([2, 2, 2, 2], 4), [(2, 2)])
        self.assertEqual(unique_pairs([2], 4), [])
        self.assertEqual(unique_pairs([], 4), [])

    def test_unique_pairs_against_brute_force(self):
        for values in itertools.combinations_with_replacement(range(-2, 3), 5):
            for target in range(-4, 5):
                expected = sorted({(values[i], values[j]) for i in range(len(values))
                                   for j in range(i + 1, len(values))
                                   if values[i] + values[j] == target})
                self.assertEqual(unique_pairs(values, target), expected)

    def test_container_examples_and_invalid_height(self):
        self.assertEqual(max_container_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(max_container_area([]), 0)
        self.assertEqual(max_container_area([3]), 0)
        with self.assertRaises(ValueError):
            max_container_area([1, -1, 2])

    def test_container_against_all_pairs(self):
        for heights in itertools.product(range(4), repeat=5):
            expected = max((j - i) * min(heights[i], heights[j])
                           for i in range(5) for j in range(i + 1, 5))
            self.assertEqual(max_container_area(heights), expected)


if __name__ == "__main__":
    unittest.main()
