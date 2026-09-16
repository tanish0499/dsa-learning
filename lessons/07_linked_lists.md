# 07 - Linked Lists

A linked list is a chain of nodes. Each node stores:

1. a value;
2. a reference to the next node.

```text
head
 |
 v
+---+---+    +---+---+    +---+------+
| 4 | o----->| 7 | o----->| 2 | None |
+---+---+    +---+---+    +---+------+
```

The nodes do not need to sit beside one another in memory. The arrows create
their order.

## The Node Class

```python
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
```

`head` stores the first node. An empty linked list has:

```python
head = None
```

## Traversal

Unlike an array, a linked list does not provide direct access by index. Begin
at `head` and follow one arrow at a time:

```python
current = head

while current is not None:
    process(current.value)
    current = current.next
```

Visualize `current` as a finger pointing at one node:

```text
current
   |
   v
 [4] -> [7] -> [2] -> None
```

After `current = current.next`:

```text
        current
           |
           v
 [4] -> [7] -> [2] -> None
```

## Exact Paper Trace

For every loop iteration, write:

```text
Step | current value | next value | answer/state after processing
```

For `[4, 7, 2]`:

```text
Step   current   next    count
start  4         7       0
1      4         7       1
2      7         2       2
3      2         None    3
end    None              3
```

Do not draw only the values. Draw the arrows, `head`, and every temporary
pointer used by the algorithm.

## Changing Links

To remove the node containing `7`:

```text
before: [4] -> [7] -> [2]

change 4.next so it points to 2

after:  [4] --------> [2]
```

The node before the removed node must be available, because its `next`
reference is what changes.

## Reversing Links

Before changing `current.next`, save the original next node. Otherwise, the
rest of the list becomes unreachable.

```python
previous = None
current = head

while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
```

Draw these four columns on paper:

```text
previous | current | saved next | link changed to
```

The movement order matters:

```text
save next -> reverse arrow -> move previous -> move current
```

## Slow And Fast Pointers

Two pointers can move at different speeds:

```python
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
```

When `fast` reaches the end, `slow` is around the middle. If the list contains
a cycle, fast and slow eventually meet.

## Complexity

```text
Read/update the head:        O(1)
Insert after a known node:   O(1)
Find a value or index:       O(n)
Traverse the whole list:     O(n)
```

## Questions Before Coding

1. Which node does each pointer currently reference?
2. Which arrow will be changed?
3. Must the original next node be saved first?
4. Can `head` itself change?
5. What happens when the list is empty or contains one node?

## First Hand Trace

Draw this list and trace its length without code:

```text
head -> [5] -> [8] -> [3] -> None
```

Then trace whether it contains `8`, followed by whether it contains `6`.
