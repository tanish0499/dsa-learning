# 04 - Sliding Window

A sliding window is a continuous section of an array or string that we track
while it moves.

Draw brackets around the active section:

```text
values: [2, 1, 5, 1, 3, 2]
         [-----]
window:   2  1  5
```

## Why Use A Window?

Suppose we need the sum of every three-value section.

A brute-force solution adds all three values again for every section:

```text
2 + 1 + 5 = 8
    1 + 5 + 1 = 7
        5 + 1 + 3 = 9
            1 + 3 + 2 = 6
```

But neighboring windows share most of their values. When the window moves one
step:

```text
old window: [2, 1, 5]       sum = 8
new window:    [1, 5, 1]

remove outgoing 2: 8 - 2 = 6
add incoming 1:    6 + 1 = 7
```

The central picture is:

```text
new state = old state - outgoing value + incoming value
```

## Fixed-Size Window

The window always contains exactly `k` values.

Typical questions:

- maximum sum among all sections of size `k`;
- number of vowels in every substring of length `k`;
- whether duplicates occur within `k` positions.

Useful positions:

```python
left = 0

for right in range(len(values)):
    # add values[right] to the window

    if right - left + 1 > k:
        # remove values[left]
        left += 1

    if right - left + 1 == k:
        # inspect the complete window
```

`right - left + 1` is the number of values inside the window.

## Variable-Size Window

Sometimes the window grows until it breaks a rule, then shrinks until the rule
is valid again.

Example: longest section with sum at most `7`, using non-negative numbers.

```text
values: [2, 1, 4, 1, 1]

[2]             sum 2: valid, expand
[2, 1]          sum 3: valid, expand
[2, 1, 4]       sum 7: valid, expand
[2, 1, 4, 1]    sum 8: too large, shrink from left
   [1, 4, 1]    sum 6: valid again
```

Basic shape:

```python
left = 0

for right in range(len(values)):
    # include the right value

    while window_breaks_rule:
        # remove the left value
        left += 1

    # the window is valid here
```

## Window Versus Two Pointers

Both techniques use pointer positions. The difference is what you visualize:

```text
Two pointers:   two important individual positions
Sliding window: every value between left and right is one active section
```

## Three Questions Before Coding

1. What information does the current window store: sum, count, set, or dictionary?
2. When should the right side expand?
3. When and why should the left side shrink?

## Complexity

For a normal sliding window, each value enters once and leaves once. Even with
a `while` loop inside a `for` loop, total work is usually `O(n)` because `left`
never moves backward.

## First Hand Trace

For `[2, 1, 5, 1, 3, 2]` and `k = 3`, make this table before coding:

```text
left | right | incoming | outgoing | window sum
```

Your expected window sums are `[8, 7, 9, 6]`.
