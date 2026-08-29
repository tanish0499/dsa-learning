"""
Mixed practice for arrays, strings, sets, dictionaries, two pointers, and
sliding windows.

The prompts intentionally do not name the intended technique.

Implement one function at a time, then run:

python -m unittest discover -s exercises/python
"""

def common_unique_values(first, second):
    """
    Return values that occur in both lists, once each, in the order they first
    appear in first.

    Example:
    [4, 2, 4, 1, 3], [3, 4, 4] -> [4, 3]
    """
    raise NotImplementedError

def is_subsequence(candidate, text):
    """
    Return True if candidate can be made by deleting characters from text
    without changing the order of the remaining characters.

    Example:
    candidate="ace", text="abcde" -> True
    candidate="aec", text="abcde" -> False
    """
    raise NotImplementedError

def first_nearby_repeat(nums, k):
    """
    Return the first value encountered whose previous equal value is at most k
    indices behind it. Return None if no such value exists.

    Example:
    [5, 1, 2, 1, 5], k=2 -> 1
    """
    raise NotImplementedError

def pair_with_difference_sorted(nums, difference):
    """
    Return True if two different positions have the given difference.

    nums is sorted in ascending order and difference is non-negative.

    Example:
    [1, 3, 5, 8], difference=3 -> True because 8 - 5 = 3
    """
    raise NotImplementedError

def count_distinct_windows(text, k):
    """
    Return the number of length-k substrings containing no repeated character.

    Return 0 when k <= 0 or k is larger than text.

    Example:
    text="abac", k=3 -> 1 because only "bac" has distinct characters
    """
    raise NotImplementedError

def maximum_sum_distinct_window(nums, k):
    """
    Return the largest sum of a length-k window whose values are all distinct.

    Return None when k <= 0, k is larger than nums, or no window qualifies.

    Example:
    [1, 5, 4, 2, 9, 9, 9], k=3 -> 15 from [4, 2, 9]
    """
    raise NotImplementedError

def longest_subarray_at_most_k_distinct(nums, k):
    """
    Return the longest continuous length containing at most k distinct values.

    Return 0 when k <= 0.

    Example:
    [1, 2, 1, 2, 3], k=2 -> 4 from [1, 2, 1, 2]
    """
    raise NotImplementedError

def shortest_window_containing_required(nums, required):
    """
    Return the smallest continuous length containing every distinct value in
    required at least once. Return 0 if no window qualifies or required is empty.

    Example:
    nums=[1, 2, 2, 3, 1, 2], required=[1, 3] -> 2 from [3, 1]
    """
    raise NotImplementedError

def closest_pair_sum_sorted(nums, target):
    """
    Return the sum of two different positions that is closest to target.

    nums is sorted. Return None when fewer than two values exist. If two sums
    are equally close, return the smaller sum.

    Example:
    [1, 3, 4, 7, 10], target=15 -> 14 from 4 + 10
    """
    raise NotImplementedError

def longest_consecutive_run(nums):
    """
    Return the length of the longest run of consecutive integer values.

    Input order does not matter and repeated values count once. Aim for O(n)
    time without calling sort() or sorted().

    Example:
    [100, 4, 200, 1, 3, 2] -> 4 from 1, 2, 3, 4
    """
    raise NotImplementedError
