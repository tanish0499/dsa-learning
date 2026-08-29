"""
Sliding window exercises.

Implement one function at a time, then run:

python -m unittest discover -s exercises/python
"""

def fixed_window_sums(nums, k):
    """
    Return the sum of every continuous window of exactly k values.

    Return [] when k <= 0 or k is larger than nums.

    Example:
    [2, 1, 5, 1, 3, 2], k=3 -> [8, 7, 9, 6]
    """
    raise NotImplementedError

def max_sum_fixed_window(nums, k):
    """
    Return the largest sum among all continuous windows of size k.

    Return None when k <= 0 or k is larger than nums.
    Do not recalculate each complete window from scratch.

    Example:
    [2, 1, 5, 1, 3, 2], k=3 -> 9
    """
    raise NotImplementedError

def count_windows_at_least(nums, k, threshold):
    """
    Return how many size-k windows have a sum at least threshold.

    Return 0 when k <= 0 or k is larger than nums.

    Example:
    [2, 1, 5, 1, 3, 2], k=3, threshold=8 -> 2
    """
    raise NotImplementedError

def max_vowels_in_window(text, k):
    """
    Return the largest number of vowels in any substring of length k.

    Treat a, e, i, o, and u as vowels and ignore case.
    Return 0 when k <= 0 or k is larger than text.

    Example:
    "abciiidef", k=3 -> 3
    """
    raise NotImplementedError

def has_nearby_duplicate(nums, k):
    """
    Return True if equal values occur at indices at most k apart.

    Keep a set representing the most recent k values.

    Example:
    [1, 2, 3, 1], k=3 -> True
    [1, 2, 3, 1], k=2 -> False
    """
    raise NotImplementedError

def smallest_subarray_at_least(nums, target):
    """
    Return the smallest length whose continuous sum is at least target.

    nums contains only positive integers. Return 0 if no window qualifies.

    Example:
    [2, 3, 1, 2, 4, 3], target=7 -> 2 because [4, 3]
    """
    raise NotImplementedError

def longest_subarray_at_most(nums, limit):
    """
    Return the longest length whose continuous sum is at most limit.

    nums contains only non-negative integers.

    Example:
    [2, 1, 4, 1, 1], limit=7 -> 4 because [1, 4, 1, 1] sums to 7
    """
    raise NotImplementedError

def longest_unique_substring(text):
    """
    Return the length of the longest substring without repeated characters.

    Example:
    "abcabcbb" -> 3 because "abc" has no repeats
    """
    raise NotImplementedError

def find_anagram_indices(text, pattern):
    """
    Return start indices where an anagram of pattern occurs in text.

    Example:
    text="cbaebabacd", pattern="abc" -> [0, 6]
    """
    raise NotImplementedError

def longest_repeating_after_replacements(text, k):
    """
    Return the longest substring that can become one repeated character after
    replacing at most k characters.

    Example:
    text="AABBABBA", k=1 -> 4
    """
    raise NotImplementedError
