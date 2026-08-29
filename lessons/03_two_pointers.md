# 03 - Two Pointers

Two pointers means keeping track of two positions while scanning data.

Do not begin with code. First draw the values and place two arrows under them.

## Picture 1 - Pointers Moving Toward Each Other

Consider this sorted list and target `10`:

```text
values: [1, 3, 4, 6, 8]
         L           R

1 + 8 = 9, which is too small.
Move L right to get a larger sum.

values: [1, 3, 4, 6, 8]
            L        R

3 + 8 = 11, which is too large.
Move R left to get a smaller sum.

values: [1, 3, 4, 6, 8]
            L     R

3 + 6 = 9, so move L right.

values: [1, 3, 4, 6, 8]
               L  R

4 + 6 = 10, so the pair exists.
```

This works because the list is sorted. Moving left rightward increases the
value; moving right leftward decreases the value.

Basic shape:

```python
left = 0
right = len(values) - 1

while left < right:
    # inspect values[left] and values[right]
    # move one of the pointers
```

## Picture 2 - Pointers Moving In The Same Direction

Sometimes one pointer reads and the other marks where the next useful value
should be written.

For `[1, 1, 2, 2, 3]`:

```text
read:   visits every value
write:  moves only when a new value is found

result being built: [1, 2, 3]
```

This is often called a read/write or slow/fast pattern.

## How To Recognize The Pattern

Think about two pointers when:

- the input is sorted;
- you compare values at two ends;
- you need a pair with a certain sum;
- you reverse or check a palindrome;
- one pointer reads while another builds a compact result;
- two sorted lists must be merged.

## Pointer Movement Is The Main Decision

For every loop, say these three things before writing code:

1. What does each pointer represent?
2. When does each pointer move?
3. When does the loop stop?

If a pointer does not move on some path, the loop may run forever.

## Complexity Picture

Even if two pointers are used, the algorithm can still be `O(n)`.
Each pointer usually crosses the data only once.

```text
Nested loops: a pointer may restart many times -> often O(n^2)
Two pointers: both keep moving forward/inward -> often O(n)
```

## First Hand Traces

Before coding, trace these on paper:

1. Reverse `[10, 20, 30, 40]` by swapping the two ends.
2. Check whether `"level"` is a palindrome.
3. Find whether `[1, 2, 4, 7, 9]` contains a pair summing to `11`.

Write the values of `left`, `right`, and the decision made at every step.
