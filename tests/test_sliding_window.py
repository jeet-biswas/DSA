import itertools
import unittest

from algorithms.sliding_window import longest_distinct_window, max_window_sum


class SlidingWindowTests(unittest.TestCase):
    def test_fixed_window_negative_and_boundary_cases(self):
        self.assertEqual(max_window_sum([-8, -3, -5], 2), -8)
        self.assertEqual(max_window_sum([2, -1, 4], 1), 4)
        self.assertEqual(max_window_sum([2, -1, 4], 3), 5)

    def test_invalid_window_sizes(self):
        for values, size in [([], 1), ([1, 2], 0), ([1, 2], -1), ([1, 2], 3)]:
            with self.subTest(values=values, size=size), self.assertRaises(ValueError):
                max_window_sum(values, size)

    def test_distinct_window_does_not_move_left_backwards(self):
        self.assertEqual(longest_distinct_window("abba"), 2)
        self.assertEqual(longest_distinct_window("abcabcbb"), 3)
        self.assertEqual(longest_distinct_window(""), 0)
        self.assertEqual(longest_distinct_window("bbbb"), 1)
        self.assertEqual(longest_distinct_window([1, 2, 1, 3]), 3)

    def test_windows_against_brute_force(self):
        for length in range(1, 6):
            for values in itertools.product([-1, 0, 1], repeat=length):
                for size in range(1, length + 1):
                    expected = max(sum(values[start:start + size])
                                   for start in range(length - size + 1))
                    self.assertEqual(max_window_sum(values, size), expected)
                expected_distinct = max(right - left
                                        for left in range(length)
                                        for right in range(left + 1, length + 1)
                                        if len(set(values[left:right])) == right - left)
                self.assertEqual(longest_distinct_window(values), expected_distinct)


if __name__ == "__main__":
    unittest.main()
