import itertools
import random
import unittest

from algorithms.sorting import insertion_sort, merge_sort


class SortingTests(unittest.TestCase):
    def test_empty_singleton_negative_and_duplicate_values(self):
        for sort in [insertion_sort, merge_sort]:
            for values in [[], [1], [3, -1, 3, 0, -4], [1, 2, 3], [3, 2, 1]]:
                with self.subTest(sort=sort.__name__, values=values):
                    result = sort(values)
                    self.assertEqual(result, sorted(values))
                    self.assertIsNot(result, values)

    def test_input_is_preserved_and_iterators_are_supported(self):
        for sort in [insertion_sort, merge_sort]:
            values = [3, 1, 2]
            self.assertEqual(sort(iter(values)), [1, 2, 3])
            sort(values)
            self.assertEqual(values, [3, 1, 2])

    def test_exhaustive_small_inputs_against_builtin_sort(self):
        for length in range(6):
            for values in itertools.product([-1, 0, 1], repeat=length):
                for sort in [insertion_sort, merge_sort]:
                    self.assertEqual(sort(values), sorted(values))

    def test_stability_keeps_equal_objects_in_original_order(self):
        class TaggedInt(int):
            pass

        values = [TaggedInt(2), TaggedInt(1), TaggedInt(2), TaggedInt(1)]
        expected = sorted(values)
        for sort in [insertion_sort, merge_sort]:
            self.assertEqual([id(value) for value in sort(values)],
                             [id(value) for value in expected])

    def test_larger_deterministic_sample(self):
        randomizer = random.Random(42)
        values = [randomizer.randrange(-1000, 1001) for _ in range(300)]
        self.assertEqual(insertion_sort(values), sorted(values))
        self.assertEqual(merge_sort(values), sorted(values))


if __name__ == "__main__":
    unittest.main()
