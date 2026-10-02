"""Stack matching, monotonic stacks, and a queue built from two stacks."""

from collections.abc import Sequence
from typing import Generic, TypeVar

T = TypeVar("T")


def brackets_balanced(text: str) -> bool:
    """Match (), [], and {} while ignoring other characters.

    O(n) time and O(n) extra space. This is a delimiter exercise, not a code
    parser: brackets inside quoted strings are still considered brackets.
    """
    opening = []
    matching = {")": "(", "]": "[", "}": "{"}
    for character in text:
        if character in "([{":
            opening.append(character)
        elif character in matching:
            if not opening or opening.pop() != matching[character]:
                return False
    return not opening


def next_greater_values(values: Sequence[int]) -> list[int | None]:
    """First STRICTLY greater value to the right of each position, or None.

    A decreasing stack stores unresolved indices. Each enters/exits at most
    once, yielding O(n) time and O(n) extra space, including the output.
    """
    result: list[int | None] = [None] * len(values)
    unresolved: list[int] = []
    for index, value in enumerate(values):
        while unresolved and values[unresolved[-1]] < value:
            result[unresolved.pop()] = value
        unresolved.append(index)
    return result


class TwoStackQueue(Generic[T]):
    """A FIFO queue with O(1) amortized enqueue, dequeue, and peek.

    A single peek/dequeue may cost O(n) when transferring between stacks, but
    each element transfers at most once. Space is O(n). Not thread-safe.
    """

    def __init__(self) -> None:
        self._incoming: list[T] = []
        self._outgoing: list[T] = []

    def __len__(self) -> int:
        return len(self._incoming) + len(self._outgoing)

    def enqueue(self, value: T) -> None:
        self._incoming.append(value)

    def _prepare_front(self) -> None:
        if not self._outgoing:
            while self._incoming:
                self._outgoing.append(self._incoming.pop())
        if not self._outgoing:
            raise IndexError("queue is empty")

    def peek(self) -> T:
        """Inspect the oldest element without removing it; raise if empty."""
        self._prepare_front()
        return self._outgoing[-1]

    def dequeue(self) -> T:
        """Remove the oldest element; raise IndexError if empty."""
        self._prepare_front()
        return self._outgoing.pop()
