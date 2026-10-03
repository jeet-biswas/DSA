# Original notebook map

The original notebooks are preserved as exploratory notes, including unfinished
ones. The Python modules add defined input/output contracts and executable tests.

| Original notebook | Companion module |
| --- | --- |
| [Traversal](../arrays/traversal.ipynb) | [Traversal](../algorithms/traversal.py) |
| [Binary search](../arrays/Searching/Binary_search.ipynb) | [Binary search](../algorithms/binary_search.py) |
| [Prefix sums](../arrays/Prefix_sum/prefix_sum.ipynb) | [Prefix sums](../algorithms/prefix_sum.py) |
| [Frequency counting](../arrays/Hasing/Frequency%20Counting.ipynb) | [Hashing](../algorithms/hashing.py) |
| [Membership](../arrays/Hasing/Existance_membership.ipynb) | [Hashing](../algorithms/hashing.py) |
| [Opposite-direction pointers](../arrays/Two_pointers/opposite_direction.ipynb) | [Two pointers](../algorithms/two_pointers.py) |

The historical `Hasing` and `Existance_membership` names are retained to avoid
breaking existing paths. Sliding windows, stacks/queues, and sorting are new
companion topics.

The prefix-sum notebook uses inclusive query endpoints. The reusable API uses
Python-style half-open endpoints: notebook query `[L, R]` becomes
`PrefixSums(values).range_sum(L, R + 1)`.

Notebook cells may depend on variables created in earlier cells. Run them in
order when studying them. The test suite exercises the standalone Python
modules; it does not execute or validate notebook output cells.
