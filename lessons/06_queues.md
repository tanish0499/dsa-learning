# 06 - Queues

A queue stores values in first-in, first-out order, shortened to FIFO.

Visualize people waiting in one line:

```text
remove here                               add here
    |                                         |
    v                                         v
 front -> [A] [B] [C] <- back
```

`A` entered first, so `A` must leave first.

## Queue Versus Stack

```text
Stack: last value added leaves first   (LIFO)
Queue: first value added leaves first  (FIFO)
```

Use a stack for nested or most-recent work. Use a queue for arrival order,
waiting lines, fair scheduling, or processing work level by level.

## Python Queue Operations

Use `collections.deque`:

```python
from collections import deque

queue = deque()

queue.append("A")     # add at the back
queue.append("B")

front = queue[0]      # inspect without removing
served = queue.popleft()
```

`append()` and `popleft()` are `O(1)`.

Avoid using this for a queue:

```python
values.pop(0)
```

Removing index `0` from a list shifts all remaining values and costs `O(n)`.

## Exact Paper Drawing

Draw the queue horizontally after every operation. The left side is always the
front and the right side is always the back:

```text
Action       Queue before   Queue after    Returned
start        []             []
enqueue A    []             [A]
enqueue B    [A]            [A, B]
enqueue C    [A, B]         [A, B, C]
dequeue      [A, B, C]      [B, C]         A
peek         [B, C]         [B, C]         B
```

Never choose an arbitrary item to remove. A normal queue can remove only its
front item.

## Queue Simulation Pattern

```python
from collections import deque

queue = deque(starting_values)

while queue:
    current = queue.popleft()

    # Process current.

    if current_needs_more_work:
        queue.append(current)
```

An item can leave the front and return at the back. This is useful for repeated
turns, ticket lines, and round-robin scheduling.

## Queue With Supporting State

The queue stores order, but another variable may store additional information:

```text
Queue       -> which value leaves next
Dictionary  -> how many copies currently exist
Running sum -> total of values currently inside
```

For example, a moving average can keep recent values in a queue and their sum
in a number. When the queue becomes too large, remove its front value and
subtract that value from the sum.

## Questions Before Coding

1. What does one queue entry represent?
2. What is added at the back?
3. What leaves from the front?
4. Can an item return to the back after processing?
5. What additional state must be updated when an item leaves?

## First Hand Trace

Trace these actions before coding:

```text
enqueue 4, enqueue 7, dequeue, enqueue 2, peek, dequeue, dequeue
```

Use this table:

```text
Action | Queue before | Queue after | Returned value
```
