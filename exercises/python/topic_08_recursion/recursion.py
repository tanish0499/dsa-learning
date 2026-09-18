"""Recursion practice. Follow the staged order in README.md.

Use recursion for every exercise. All supplied inputs satisfy the docstrings.
Do not mutate inputs. Start with small examples and draw each call and return.
"""


def count_down(n):
    """Return [n, ..., 1] recursively. n is an integer >= 0; 0 returns []."""
    raise NotImplementedError


def count_up(n):
    """Return [1, ..., n] recursively. n is an integer >= 0; 0 returns []."""
    raise NotImplementedError


def sum_to_n(n):
    """Return 1 + ... + n. n is an integer >= 0; 0 returns 0."""
    raise NotImplementedError


def sum_even_to_n(n):
    """Sum the even integers from 0 through n inclusive. n >= 0.
    Example: n=5 returns 6 (2 + 4)."""
    raise NotImplementedError


def factorial(n):
    """Return n factorial for integer n >= 0. 0! = 1.
    Example: 4 returns 24 (4 * 3 * 2 * 1)."""
    raise NotImplementedError


def power(base, exponent):
    """Return base raised to integer exponent >= 0 using recursive multiplication.
    Return 1 for exponent 0, including base 0. Do not use ** or pow()."""
    raise NotImplementedError


def sum_digits(n):
    """Return the sum of decimal digits in integer n >= 0.
    Example: 402 returns 6. Zero returns 0."""
    raise NotImplementedError


def count_digits(n):
    """Return the number of decimal digits in integer n >= 0.
    Example: 402 returns 3. Zero has ONE digit."""
    raise NotImplementedError


def sum_values(values):
    """Return the recursive sum of integer values; [] returns 0.
    Do not use sum(). Leave the input unchanged."""
    raise NotImplementedError


def count_target(values, target):
    """Return how often target occurs; [] returns 0.
    Do not use list.count(). Leave the input unchanged."""
    raise NotImplementedError


def contains_value(values, target):
    """Recursively check whether target exists; [] returns False.
    Compare one value per call instead of using membership on the whole list."""
    raise NotImplementedError


def maximum_value(values):
    """Return the largest integer, or None for [].
    Values may all be negative. Do not call max() on the list."""
    raise NotImplementedError


def first_index(values, target):
    """Return the first zero-based index of target, or -1 if absent.
    Do not use list.index(). Leave the input unchanged."""
    raise NotImplementedError


def reverse_text(text):
    """Return text reversed recursively. Empty text returns ''.
    Do not use reversed(), reverse(), or negative-step slicing."""
    raise NotImplementedError


def count_character(text, character):
    """Return occurrences of character (a one-character string).
    Comparison is case-sensitive. Do not use str.count()."""
    raise NotImplementedError


def remove_character(text, character):
    """Return text with all occurrences of character removed.
    character has length 1; comparison is case-sensitive. Do not use replace()."""
    raise NotImplementedError


def is_palindrome(text):
    """Recursively compare matching ends. Empty and one-character strings are True.
    Compare exactly, including spaces and case. Do not reverse the string."""
    raise NotImplementedError


def is_sorted(values):
    """Return True when integer values are non-decreasing; [] is True.
    Compare neighboring values recursively. Equal neighbors are allowed."""
    raise NotImplementedError


def fibonacci(n):
    """Return F(n), with F(0)=0 and F(1)=1; n is an integer >= 0.
    Begin with two recursive calls for n >= 2. Practice only with n <= 15.
    This intentionally repeats work; optimization comes in a later lesson."""
    raise NotImplementedError


def count_stair_ways(n):
    """Return ways to climb n steps taking 1 or 2 steps each move; n >= 0.
    There is 1 way to climb 0 steps (take no steps).
    Example: 3 returns 3: [1,1,1], [1,2], [2,1]. Practice with n <= 15."""
    raise NotImplementedError
