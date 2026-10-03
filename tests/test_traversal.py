import unittest

from algorithms.traversal import linear_search, min_max, second_largest


class TraversalTests(unittest.TestCase):
    def test_search_returns_first_match_and_missing_sentinel(self):
        self.assertEqual(linear_search([4, 2, 4], 4), 0)
        self.assertEqual(linear_search([4, 2, 4], 2), 1)
        self.assertEqual(linear_search([4, 2, 4], 7), -1)
        self.assertEqual(linear_search([], 7), -1)
        self.assertEqual(linear_search("hello", "l"), 2)

    def test_min_max_negative_singleton_and_mixed_values(self):
        for values in [[-9, -4, -8], [7], [9, -2, 6, 9]]:
            with self.subTest(values=values):
                self.assertEqual(min_max(values), (min(values), max(values)))

    def test_empty_min_max_is_explicit(self):
        with self.assertRaises(ValueError):
            min_max([])

    def test_second_largest_requires_distinct_values(self):
        cases = [([], None), ([5], None), ([5, 5], None),
                 ([9, 9, 3, 6], 6), ([-4, -9, -2], -4), ([0, -1], -1)]
        for values, expected in cases:
            with self.subTest(values=values):
                self.assertEqual(second_largest(values), expected)

    def test_functions_preserve_input(self):
        values = [4, 1, 4, 2]
        original = values.copy()
        linear_search(values, 1)
        min_max(values)
        second_largest(values)
        self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
