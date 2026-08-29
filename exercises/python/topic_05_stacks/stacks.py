"""
Stack exercises.

Implement one function at a time, then run:

python -m unittest discover -s exercises/python
"""


def reverse_with_stack(values):
    """
    Return a new list containing values in reverse order by using a stack.

    Do not use reverse(), reversed(), or slicing with a negative step.

    Example:
    [4, 7, 2] -> [2, 7, 4]
    """
    raise NotImplementedError


def apply_backspaces(text):
    """
    Return the text remaining after every '#' removes the latest character.

    Ignore a '#' when there is no character available to remove.

    Example:
    "ab#c" -> "ac"
    "a##b" -> "b"
    """
    raise NotImplementedError


def is_balanced_parentheses(text):
    """
    Return True when (), [], and {} are correctly matched and nested.

    Ignore characters that are not brackets.

    Example:
    "a + ([b])" -> True
    "([)]" -> False
    """
    raise NotImplementedError


def remove_adjacent_duplicates(text):
    """
    Repeatedly remove neighboring equal characters and return what remains.

    Example:
    "abbaca" -> "ca"
    """
    raise NotImplementedError


def evaluate_postfix(tokens):
    """
    Evaluate a valid postfix expression containing integers and +, -, *, /.

    Division must truncate toward zero.

    Example:
    ["2", "1", "+", "3", "*"] -> 9
    """
    raise NotImplementedError


def simplify_unix_path(path):
    """
    Return the canonical absolute Unix path.

    Ignore empty parts and '.', and let '..' remove one directory when possible.

    Example:
    "/home//ops/../logs/" -> "/home/logs"
    """
    raise NotImplementedError


def validate_stack_sequences(pushed, popped):
    """
    Return True if popped can result from pushing values in pushed order.

    Example:
    pushed=[1, 2, 3], popped=[2, 3, 1] -> True
    """
    raise NotImplementedError


def next_greater_values(nums):
    """
    For each value, return the first greater value to its right, or -1.

    Aim for O(n) after first writing or tracing a brute-force approach.

    Example:
    [2, 1, 5, 3] -> [5, 5, -1, -1]
    """
    raise NotImplementedError


def daily_warmer_waits(temperatures):
    """
    Return how many positions each value must wait for a warmer value.

    Return 0 where no later warmer value exists.

    Example:
    [73, 74, 71, 75] -> [1, 2, 1, 0]
    """
    raise NotImplementedError


def stock_spans(prices):
    """
    Return each price's span of consecutive earlier-or-equal prices.

    The current day is included in its span.

    Example:
    [100, 80, 60, 70, 60, 75, 85] -> [1, 1, 1, 2, 1, 4, 6]
    """
    raise NotImplementedError
