# Sliding Window - `if` Or `while`?

## Fast Rule

```text
Use if when at most one removal is needed.
Use while when removals must repeat until a condition changes.
```

## Fixed-Size Window

Use `if` when the required window size is exactly `k`.

Before adding the incoming value, the window has at most `k` values. Adding one
value makes it at most `k + 1`, so one removal is enough.

```python
for right in range(len(values)):
    add(values[right])

    if right - left + 1 > k:
        remove(values[left])
        left += 1

    if right - left + 1 == k:
        inspect_window()
```

Common examples:

- sum of every size-`k` window;
- maximum vowels in a size-`k` substring;
- anagram windows;
- number of size-`k` windows with distinct values.

## Variable-Size Valid Window

Use `while` when adding one value may require several removals before the
window becomes valid again.

```python
for right in range(len(values)):
    add(values[right])

    while window_is_invalid:
        remove(values[left])
        left += 1

    inspect_valid_window()
```

Common examples:

- longest substring without repeated characters;
- longest window with at most `k` distinct values;
- longest non-negative subarray with sum at most a limit.

## Smallest Qualifying Window

Sometimes the window is valid, but we keep shrinking to find every smaller
valid candidate.

```python
for right in range(len(values)):
    add(values[right])

    while window_is_valid:
        record_current_size()
        remove(values[left])
        left += 1
```

Example: smallest positive-number subarray with sum at least a target.

## Decision Checklist

```text
Is the required size exactly k?
    Yes -> if size > k, remove once.

Is size controlled by a validity rule?
    Yes -> while invalid, keep removing.

Am I finding the smallest valid window?
    Yes -> while valid, record and keep removing.
```

The nested `while` normally remains `O(n)` because `left` only moves forward.
Each value enters and leaves the window at most once.
