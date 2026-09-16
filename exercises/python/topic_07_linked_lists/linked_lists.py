"""
Linked-list exercises.

Implement one function at a time, then run:

python -m unittest discover -s exercises/python
"""


class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def build_linked_list(values):
    """Build a linked list from values and return its head."""
    head = None
    tail = None

    for value in values:
        node = ListNode(value)

        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head


def linked_list_to_list(head):
    """Return linked-list values as a normal list. Do not use on a cycle."""
    values = []
    current = head

    while current is not None:
        values.append(current.value)
        current = current.next

    return values


def linked_list_length(head):
    """
    Return the number of nodes reachable from head.

    Example:
    4 -> 7 -> 2 -> None returns 3
    """
    raise NotImplementedError


def contains_value(head, target):
    """
    Return True when target occurs in the linked list.

    Example:
    4 -> 7 -> 2 -> None, target=7 returns True
    """
    raise NotImplementedError


def value_at_index(head, index):
    """
    Return the value at the zero-based index, or None when it does not exist.

    Return None for a negative index.

    Example:
    4 -> 7 -> 2 -> None, index=1 returns 7
    """
    raise NotImplementedError


def append_value(head, value):
    """
    Add a new node at the end and return the possibly new head.

    Example:
    4 -> 7 -> None, value=2 becomes 4 -> 7 -> 2 -> None
    """
    raise NotImplementedError


def delete_first_value(head, target):
    """
    Delete only the first node containing target and return the new head.

    Leave the list unchanged when target is absent.

    Example:
    1 -> 2 -> 1 -> None, target=1 becomes 2 -> 1 -> None
    """
    raise NotImplementedError


def reverse_linked_list(head):
    """
    Reverse the links in place and return the new head.

    Example:
    1 -> 2 -> 3 -> None becomes 3 -> 2 -> 1 -> None
    """
    raise NotImplementedError


def middle_value(head):
    """
    Return the middle node's value, or None for an empty list.

    For an even number of nodes, return the second middle value.

    Example:
    1 -> 2 -> 3 -> 4 -> None returns 3
    """
    raise NotImplementedError


def merge_sorted_lists(first, second):
    """
    Merge two ascending linked lists and return the merged head.

    Reuse the existing nodes rather than creating a list of their values.

    Example:
    1 -> 3 and 2 -> 4 become 1 -> 2 -> 3 -> 4
    """
    raise NotImplementedError


def remove_nth_from_end(head, n):
    """
    Remove the nth node from the end and return the new head.

    Leave the list unchanged when n <= 0 or n exceeds the list length.

    Example:
    1 -> 2 -> 3 -> 4 -> 5, n=2 becomes 1 -> 2 -> 3 -> 5
    """
    raise NotImplementedError


def has_cycle(head):
    """
    Return True when following next references eventually revisits a node.

    Aim for O(1) extra space by using slow and fast pointers.
    """
    raise NotImplementedError
