"""
Queue exercises.

Implement one function at a time, then run:

python -m unittest discover -s exercises/python
"""


def process_queue_operations(operations):
    """
    Process (operation, value) pairs using a queue.

    Supported operations are "enqueue", "dequeue", and "peek". The value is
    ignored for dequeue and peek. Return the results produced by every dequeue
    and peek. Return None for those operations when the queue is empty.

    Example:
    [("enqueue", 10), ("enqueue", 20), ("dequeue", None),
     ("peek", None)] -> [10, 20]
    """
    raise NotImplementedError


def serve_customers(customers, count):
    """
    Serve at most count customers in FIFO order.

    Return (served, waiting), where both values are lists. When count is zero
    or negative, no customer is served.

    Example:
    ["A", "B", "C"], count=2 -> (["A", "B"], ["C"])
    """
    raise NotImplementedError


def last_n_events(events, n):
    """
    Return the latest n events in their original order.

    Return [] when n <= 0.

    Example:
    ["a", "b", "c", "d"], n=2 -> ["c", "d"]
    """
    raise NotImplementedError


def reverse_first_k(values, k):
    """
    Reverse the first k queue values while preserving the remaining order.

    Return values unchanged when k <= 0 or k is larger than values.

    Example:
    [1, 2, 3, 4, 5], k=3 -> [3, 2, 1, 4, 5]
    """
    raise NotImplementedError


def moving_averages(values, k):
    """
    Return the average of every continuous window containing k values.

    Do not recalculate each window's sum from scratch. Return [] when k <= 0
    or k is larger than values.

    Example:
    [1, 2, 3, 4], k=3 -> [2.0, 3.0]
    """
    raise NotImplementedError


def first_non_repeating_stream(text):
    """
    After each character arrives, report the first character seen exactly once.

    Use None when no non-repeating character exists.

    Example:
    "aabc" -> ["a", None, "b", "b"]
    """
    raise NotImplementedError


def time_to_buy_tickets(tickets, k):
    """
    Return the seconds until the person originally at index k finishes.

    Each second, the front person buys one ticket. A person needing more
    tickets returns to the back; otherwise that person leaves.

    Example:
    [2, 3, 2], k=2 -> 6
    """
    raise NotImplementedError


def round_robin_completion_order(tasks, quantum):
    """
    Return task names in the order they complete under round-robin scheduling.

    Each task is a (name, duration) pair. A turn performs at most quantum units
    of work; unfinished tasks return to the back.

    Example:
    [("A", 3), ("B", 1), ("C", 2)], quantum=2 -> ["B", "C", "A"]
    """
    raise NotImplementedError


def generate_binary_numbers(n):
    """
    Return binary representations of the integers from 1 through n.

    Generate them with a queue rather than calling bin(). Return [] for n <= 0.

    Example:
    n=5 -> ["1", "10", "11", "100", "101"]
    """
    raise NotImplementedError


def sliding_window_maximum(nums, k):
    """
    Return the maximum value from every continuous window of size k.

    Aim for O(n) with a deque after first tracing a brute-force solution.
    Return [] when k <= 0 or k is larger than nums.

    Example:
    [1, 3, -1, -3, 5, 3, 6, 7], k=3 -> [3, 3, 5, 5, 6, 7]
    """
    raise NotImplementedError
