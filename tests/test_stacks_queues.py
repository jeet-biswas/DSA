from collections import deque
import itertools
import random
import unittest

from algorithms.stacks_queues import TwoStackQueue, brackets_balanced, next_greater_values


class StackQueueTests(unittest.TestCase):
    def test_balanced_nested_and_mismatched_brackets(self):
        for text in ["", "plain text", "{a + (b * [c])}", "()[]{}"]:
            self.assertTrue(brackets_balanced(text), text)
        for text in ["([)]", "(()", ")(", "}", "["]:
            self.assertFalse(brackets_balanced(text), text)

    def test_next_greater_is_strict_and_first(self):
        self.assertEqual(next_greater_values([2, 2, 3, 5]), [3, 3, 5, None])
        self.assertEqual(next_greater_values([-3, -1, -2]), [-1, None, None])
        self.assertEqual(next_greater_values([]), [])

    def test_next_greater_against_brute_force(self):
        for values in itertools.product(range(3), repeat=5):
            expected = [next((value for value in values[index + 1:] if value > current), None)
                        for index, current in enumerate(values)]
            self.assertEqual(next_greater_values(values), expected)

    def test_empty_queue_errors_and_none_payload(self):
        queue = TwoStackQueue()
        self.assertEqual(len(queue), 0)
        with self.assertRaises(IndexError):
            queue.peek()
        with self.assertRaises(IndexError):
            queue.dequeue()
        queue.enqueue(None)
        self.assertIsNone(queue.peek())
        self.assertEqual(len(queue), 1)
        self.assertIsNone(queue.dequeue())
        self.assertFalse(queue)

    def test_interleaved_queue_operations_against_deque(self):
        randomizer = random.Random(2026)
        queue = TwoStackQueue()
        reference = deque()
        for _ in range(500):
            if not reference or randomizer.random() < 0.6:
                value = randomizer.randrange(-20, 21)
                queue.enqueue(value)
                reference.append(value)
            else:
                self.assertEqual(queue.peek(), reference[0])
                self.assertEqual(queue.dequeue(), reference.popleft())
            self.assertEqual(len(queue), len(reference))
        while reference:
            self.assertEqual(queue.dequeue(), reference.popleft())
        self.assertEqual(len(queue), 0)


if __name__ == "__main__":
    unittest.main()
