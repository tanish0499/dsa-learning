# Visualizing Sliding Windows

## Do Not Visualize The Whole Program

At any moment, remember only five pieces of state:

```text
left, right, current window, supporting state, best answer
```

The current window is always:

```python
values[left:right + 1]
```

Do not try to generate every possible subarray. Generate only the windows the
two pointers visit.

## Draw The Input With Indices

```text
index:  0  1  2  3  4  5
value: [1, 2, 2, 3, 1, 2]
```

For `required = {1, 3}`, the supporting state is a frequency dictionary that
stores only required values.

## Use Two Phases

For every movement of `right`:

```text
EXPAND: move right once and add the incoming value.
CHECK:  is the window valid?
SHRINK: while valid, record it and move left once.
REPEAT: check validity again after every left movement.
```

This becomes the code shape later:

```python
for right in range(len(values)):
    add(values[right])

    while window_is_valid:
        record_window()
        remove(values[left])
        left += 1
```

## Trace One Pointer Movement Per Row

```text
Action     L  R  Window          Counts       Valid?      Best
start      0  -  []              {}           no          -
add 1      0  0  [1]             {1: 1}       no          -
add 2      0  1  [1, 2]          {1: 1}       no          -
add 2      0  2  [1, 2, 2]       {1: 1}       no          -
add 3      0  3  [1, 2, 2, 3]    {1: 1,3: 1}  yes         4
remove 1   1  3  [2, 2, 3]       {3: 1}       no          4
add 1      1  4  [2, 2, 3, 1]    {3: 1,1: 1}  yes         4
remove 2   2  4  [2, 3, 1]       {3: 1,1: 1}  yes         3
remove 2   3  4  [3, 1]          {3: 1,1: 1}  yes         2
remove 3   4  4  [1]             {1: 1}       no          2
add 2      4  5  [1, 2]          {1: 1}       no          2
```

Notice the rhythm:

```text
right moves -> check -> left may move many times -> right moves again
```

## Blank Worksheet

Before coding, fill in this table for one small example:

```text
Action  L  R  Window  State  Valid?  Best
start
add
remove
```

For each row, ask only:

1. Which pointer just moved?
2. Which value entered or left?
3. How does the supporting state change?
4. Is the window valid now?
5. Should the best answer be updated?

## Turning The Trace Into Code

Each repeated action in the table becomes one code block:

```text
Every `add` row       -> outer `for right` loop
Repeated `remove` rows -> inner `while` loop
Counts column          -> dictionary updates
Best column            -> min/max update
```

You do not need to see the entire solution mentally. If you can correctly
produce the next row, the code is just the repeated rule for producing that
row.
