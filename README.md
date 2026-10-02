# Data structures and algorithms in Python

A practice repository for learning how algorithms work, when to use them, and
how to check their edge cases. The original notebooks are retained as study
notes. Reusable implementations and executable tests live alongside them.

## Start here

Use Python 3.11 or newer. The implementations and tests use only the standard
library; no packages or virtual environment are required.

From the repository root, run:

```sh
python -m unittest discover -s tests -v
```

Some Windows installations use `py -3` instead of `python`.

## Repository layout

```text
arrays/        Original exploratory Jupyter notebooks
algorithms/    Small, reusable Python implementations
tests/         Executable examples and edge-case checks
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
