# Choosing an algorithm pattern

Let `n` be the number of input values, `u` the number of distinct values, and
`p` the number of returned pairs. Hash-table costs below are expected costs.
Input sequences support constant-time indexing, as Python lists do.

| Need | Pattern / function | Time | Additional space |
| --- | --- | --- | --- |
| Find the first match in unsorted data | `linear_search` | O(n) | O(1) |
| Find extrema or a distinct runner-up | `min_max`, `second_largest` | O(n) | O(1) |
| Find a value or insertion boundary in sorted data | `binary_search`, `lower_bound`, `upper_bound` | O(log n) | O(1) |
| Count duplicates in sorted data | `count_occurrences` | O(log n) | O(1) |
| Produce cumulative totals | `running_sum` | O(n) | O(n) output |
| Answer many range sums on unchanged data | `PrefixSums` | O(n) build, O(1) query | O(n) |
| Count target-sum subarrays, including negatives | `count_subarrays_with_sum` | O(n) | O(n) |
| Find the longest zero-sum interval | `longest_zero_sum_subarray` | O(n) | O(n) |
| Count, find repeats, or locate a unique value | `frequencies`, `contains_duplicate`, `first_unique_index` | O(n) | O(u) |
| Find an unsorted pair with a target sum | `two_sum_indices` | O(n) | O(n) |
| Compare or swap from both ends | `is_palindrome`, `reverse_in_place` | O(n) | O(1) |
| List distinct target-sum pairs in sorted input | `unique_pairs` | O(n) | O(p) output |
| Find the widest useful pair of walls | `max_container_area` | O(n) | O(1) |
| Find a maximum fixed-width sum | `max_window_sum` | O(n) | O(1) |
| Find the longest duplicate-free interval | `longest_distinct_window` | O(n) | O(u) |
| Match nested delimiters | `brackets_balanced` | O(n) | O(n) |
| Find the next larger value to the right | `next_greater_values` | O(n) | O(n) |
| Implement FIFO using stack operations | `TwoStackQueue` | O(1) amortized / operation | O(n) |
| Sort a short or nearly sorted sequence | `insertion_sort` | O(n²) worst, O(n) best | O(n) returned copy |
| Sort with a predictable asymptotic bound | `merge_sort` | O(n log n) | O(n) |

## Invariants to explain before coding

- **Binary search:** the insertion position lies between `left` and `right`
  inclusive; `[left, right)` contains the elements still to examine. Values
  already excluded satisfy the chosen `<` or `<=` comparison.
- **Prefix sums:** the total before `stop` minus the total before `start`
  gives the sum of `[start, stop)`. The leading zero handles ranges from zero.
- **Two pointers:** after rejecting one endpoint, no remaining pair with that
  endpoint can solve the sorted pair-sum problem.
- **Distinct window:** the current window contains no repeats. Its left
  boundary can move forward, never backward.
- **Monotonic stack:** unresolved positions have non-increasing values. A new
  larger value resolves smaller positions while leaving equal values waiting.
- **Two-stack queue:** the outgoing stack holds the oldest items at its top.
  Transfer incoming items only after the outgoing stack becomes empty.
- **Insertion sort:** the prefix before the current index is already sorted.
- **Merge sort:** merge two sorted halves by selecting the smaller front value.

## Common traps

1. **An index is not a value.** `two_sum_indices` returns positions;
   `unique_pairs` returns values. Neither reuses a single position twice.
2. **Duplicates change the question.** The runner-up is the second distinct
   value; `[5, 5]` has no runner-up. Binary search returns the first match.
3. **Zero and negatives are real answers.** Initialize a maximum window from
   actual input, not zero. Prefix-sum counting works with negative values;
   a sum-based shrinking window needs additional assumptions.
4. **Range conventions must agree.** The original notebook uses inclusive
   `[L, R]`; call `range_sum(L, R + 1)` in the module.
5. **Unsorted data breaks binary search and sorted pair search.** These
   functions intentionally do not spend O(n) checking sortedness.
6. **A queue's amortized bound is not its worst single operation.** One
   dequeue can transfer O(n) items; each item is transferred only once.
7. **Mutation is a contract.** Only `reverse_in_place` intentionally modifies
   its provided sequence. `PrefixSums` takes a snapshot; changing the original
   sequence does not update its answers.
8. **Use missing-result conventions deliberately.** Searches return `-1`,
   missing optional values return `None`, and counts/lengths return `0`.
   Empty extrema, invalid ranges, and empty queue access raise exceptions.

## A useful practice loop

Choose a function, hide its implementation, and solve its test examples by
hand. Write a straightforward solution first. Then implement the faster
pattern, explain why discarded candidates cannot help, and compare results
against the straightforward solution on small inputs. Use complexity to
reason about growth, not as a replacement for checking correctness.
