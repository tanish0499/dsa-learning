# 08 - Recursion

Read only the first worked example and Stage 1 before starting. Later stages
can wait until the earlier movement feels familiar.

## What A Recursive Call Means

Recursion is a function asking another call of itself to solve a smaller
version of the same problem. Every call has its own local variables. The
caller pauses at that call, waits for its result, then continues.

A stack remembers the paused calls. The most recent call finishes first.

## A Complete Example: Count List Items

You already know how to count items with a loop. Here is the recursive version:

```python
def count_items(values, index=0):
    if index == len(values):
        return 0

    rest_count = count_items(values, index + 1)
    return 1 + rest_count
```

For [4, 7, 2], each call counts one item plus the remaining items.

### Going Down: Calls Wait

```text
index 0: wait for the answer from index 1
    index 1: wait for the answer from index 2
        index 2: wait for the answer from index 3
            index 3: no items remain; return 0
```

### Coming Back: Answers Return

```text
index 3 returns 0
index 2 receives 0 -> returns 1 + 0 = 1
index 1 receives 1 -> returns 1 + 1 = 2
index 0 receives 2 -> returns 1 + 2 = 3
```

The index does not move backward within one call. An older call resumes with
its own unchanged index. For example, index 2 is still 2 when it resumes.

## Exactly What To Write On Paper

Draw one row per call. Fill the final column only when that call finishes:

```text
Call       Input index   Waiting calculation   Returned answer
count      0             1 + count(index 1)    3 (fill last)
count      1             1 + count(index 2)    2
count      2             1 + count(index 3)    1
count      3             nothing               0 (fill first)
```

Start at the top and write the calls downward. Then start at the base case
and fill the returned answers upward. Trace a one-item list and an empty list
before coding anything else.

## Three Decisions Before Coding

1. What does this function promise to return for its input?
2. What is the smallest input I can answer immediately (the base case)?
3. What smaller input will I pass, and how will I use its returned answer?

For count_items:

```text
Promise: count all items from index onward.
Base case: index equals length -> return 0.
Smaller problem: count from index + 1.
Combine: one current item + count of the rest.
```

Each call must approach its base case. Calling again with the same input
without changing any state will never finish.

## Stage 1: One Smaller Number

For counting and numeric totals, start with n=0, then n=1, then n=3.
Ask what the answer for n-1 already contains and what n contributes.
Return the requested answer; do not print instead of returning.

For list-valued answers, order matters: placing the current value before the
smaller result differs from placing it after that result. Trace both orders.

## Stage 2: Different Base Cases

A sum often starts with 0, while a product starts with 1. Choose the base case
from the meaning of the question, not from a memorized template.

For digit exercises, integer division by 10 removes the last decimal digit,
and remainder modulo 10 gives that digit. Decide separately what zero means
for a digit sum and for a digit count.

## Stage 3: Lists

Use a helper with an index to represent the remaining part of a list. Keep the
public function signature unchanged. For example, the outer function can call
an inner helper starting at index 0.

Slicing a smaller list is acceptable initially for understanding, but it copies
elements. After the trace works, use indices to avoid repeatedly copying lists.
The exercises ask you to keep the original input unchanged.

## Stage 4: Strings And Neighbor Comparisons

Repeat the same ideas: process one character, combine it with the rest, or
compare matching ends. Palindrome checks can move a left and a right index
inward on every call. Sortedness checks compare one neighboring pair at a time.

## Stage 5: Two Calls (Only After The Earlier Stages)

Fibonacci and stair counting introduce branching. Draw a call tree rather
than a single column, and complete one branch before the next. These simple
versions recalculate the same answers. They are demonstrations of recursion,
not efficient solutions for large inputs. Memoization comes later.

## Cost And Limits

The count_items example takes O(n) time and O(n) call-stack space. Recursion is
not automatically faster than a loop. List concatenation or slicing can add
extra cost even when there is only one recursive call per step.

Python limits recursion depth. Use small inputs for this lesson; do not raise
the recursion limit as a fix for a missing base case.

## Common Mistakes To Check

- Calling with unchanged input.
- Forgetting to return the recursive result.
- Using a base-case value that changes the meaning of the answer.
- Assuming all calls share the same local variables.
- Trying to trace large examples before n=0, n=1, and n=3 work.
