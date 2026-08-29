# 05 - Stacks

A stack stores values in last-in, first-out order, usually shortened to LIFO.

Visualize a stack vertically. Values can be added or removed only at the top:

```text
       top
        |
        v
      +---+
      | C |  <- most recently added
      +---+
      | B |
      +---+
      | A |  <- added first
      +---+
```

Removing one value returns `C`, then `B`, then `A`.

## Python Operations

Python lists provide the stack operations we need:

```python
stack = []

stack.append("A")  # push
stack.append("B")

top = stack[-1]    # peek without removing
removed = stack.pop()
```

All three operations at the end of a list are normally `O(1)`.

Do not use `pop(0)` for a stack. Index `0` is the bottom, and removing it shifts
the remaining values.

## Paper Trace

Draw the stack after every operation:

```text
Action    Stack          Output
start     []
push A    [A]
push B    [A, B]
push C    [A, B, C]
pop       [A, B]         C
peek      [A, B]         B
```

The rightmost list value is the top of the stack.

## When A Stack Fits

Look for one of these relationships:

- the latest unfinished item must be handled first;
- opening symbols must be matched by later closing symbols;
- an undo removes the most recent action;
- values wait until a later value resolves them;
- output should occur in reverse arrival order.

## Matching Brackets

For `"([{}])"`, opening brackets wait in the stack:

```text
Read    Stack     Meaning
(       [(]       waiting for )
[       [(, []    waiting for ]
{       [(, [, {] waiting for }
}       [(, []    matches top {
]       [(]       matches top [
)       []         matches top (
```

A closing bracket is valid only when it matches the current top. Matching some
earlier opening bracket is not enough because nesting order matters.

## Values Waiting For An Answer

Some problems ask for the next larger value to the right. A stack can hold
values whose answer has not been found yet:

```text
values: [2, 1, 5]

2 waits
1 waits above 2
5 resolves 1, then resolves 2
```

This later becomes a monotonic stack: the stack is kept in increasing or
decreasing order so one incoming value can resolve several previous values.

## Questions Before Coding

1. What exactly does one stack entry represent?
2. What event pushes an entry?
3. What event pops an entry?
4. Do I need the top value, the removed value, or both?
5. What should happen if a pop is requested while the stack is empty?

## First Hand Trace

Trace these actions before starting the exercises:

```text
push 4, push 7, pop, push 2, peek, pop, pop
```

Use this table:

```text
Action | Stack before | Stack after | Returned value
```
