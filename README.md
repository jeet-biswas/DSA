# Data structures and algorithms in Python

[![Tests](https://github.com/jeet-biswas/DSA/actions/workflows/tests.yml/badge.svg)](https://github.com/jeet-biswas/DSA/actions/workflows/tests.yml)

A practice repository for learning how algorithms work, when to use them, and
how to check their edge cases. The original notebooks are retained as study
notes. Reusable implementations and executable tests live alongside them.

## Start here

Use Python 3.11 or newer. The implementations and tests use only the standard
library; no packages or virtual environment are required.

From the repository root, run:

```sh
python -m unittest discover -s tests -v
python -m examples.practice_demo
```

Some Windows installations use `py -3` instead of `python`.

## Repository layout

```text
arrays/        Original exploratory Jupyter notebooks
algorithms/    Small, reusable Python implementations
tests/         Executable examples and edge-case checks
examples/      A runnable tour of the implementations
docs/          Pattern selection and complexity notes
```

The notebook directory names are preserved so existing links keep working.
Open `.ipynb` files in Jupyter or VS Code if you want to inspect the original
experiments. Jupyter is optional and is not needed to run the Python modules.

## How to practice

1. Read a problem and write down its input assumptions.
2. Try a small example by hand, including an empty input where it makes sense.
3. Explain the invariant: what remains true after each iteration?
4. Implement the solution and run its tests.
5. Compare time and extra-space costs with a straightforward alternative.

Algorithm modules document whether they modify their inputs and whether inputs
must be sorted. An algorithm's complexity assumes those preconditions already
hold; sorting a fresh input has its own cost.

## Topic map

| Topic | Implementations | What to practice |
| --- | --- | --- |
| Traversal | [traversal.py](algorithms/traversal.py) | Search, extrema, distinct second largest |
| Binary search | [binary_search.py](algorithms/binary_search.py) | Lower/upper bounds, duplicate counts |
| Prefix sums | [prefix_sum.py](algorithms/prefix_sum.py) | Range sums, repeated prefixes, negative values |
| Hashing | [hashing.py](algorithms/hashing.py) | Frequencies, uniqueness, unsorted pair search |
| Two pointers | [two_pointers.py](algorithms/two_pointers.py) | Reversal, palindrome, distinct pairs, container area |
| Sliding window | [sliding_window.py](algorithms/sliding_window.py) | Fixed window sums, longest distinct window |
| Stacks and queues | [stacks_queues.py](algorithms/stacks_queues.py) | Bracket matching, next greater value, FIFO |
| Sorting | [sorting.py](algorithms/sorting.py) | Stable insertion sort and merge sort |

Read the [pattern guide](docs/PATTERNS.md) for preconditions, complexity, and
common mistakes. The [notebook map](docs/NOTEBOOKS.md) connects the original
exercises to the reusable code without changing the notebooks.

## Example: repeated range queries

```python
from algorithms.prefix_sum import PrefixSums

totals = PrefixSums([6, 3, 8, 2, 5, 4, 6])
print(totals.range_sum(1, 4))  # 13: indices 1, 2, 3
print(totals.range_sum(0, 7))  # 34: the complete input
```

Ranges use an exclusive end index, just like Python slices. Invalid bounds
raise `IndexError`; an empty range has sum zero.

## Checks and changes

Tests cover empty inputs, duplicates, negative values, invalid ranges, and
input mutation contracts. Selected algorithms are also compared with simple
brute-force solutions or Python's standard library on many small inputs.

GitHub Actions runs the suite on Python 3.11, 3.12, and 3.13 on Linux, plus
Python 3.13 on Windows. No third-party runtime or testing dependencies are
installed. See the workflow for the latest results.

When adding an exercise, include its assumptions, complexity, at least one
normal example and one edge case, and a test that demonstrates the behavior.
Prefer readable steps over compressed one-line solutions.
