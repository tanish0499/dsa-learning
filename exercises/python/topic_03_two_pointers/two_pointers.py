"""
Two pointers exercises.

Implement one function at a time, then run:

python -m unittest discover -s exercises/python
"""

def reverse_values(values):
    """
    Return a reversed copy of values using left and right pointers.

    Do not use slicing, reversed(), or list.reverse().

    Example:
    [1, 2, 3, 4] -> [4, 3, 2, 1]
    """
    raise NotImplementedError

def is_palindrome(text):
    """
    Return True if text reads the same forward and backward.

    Compare characters using left and right pointers.

    Example:
    "level" -> True
    "python" -> False
    """
    raise NotImplementedError

def pair_sum_sorted(nums, target):
    """
    Return True if two different positions add up to target.

    nums is sorted in ascending order.

    Example:
    [1, 2, 4, 7, 9], target 11 -> True because 2 + 9 = 11
    """
    raise NotImplementedError

def merge_sorted_lists(first, second):
    """
    Merge two sorted lists and return one sorted list.

    Use one pointer for each input list. Do not call sort() or sorted().

    Example:
    [1, 4, 7], [2, 3, 8] -> [1, 2, 3, 4, 7, 8]
    """
    raise NotImplementedError

def remove_duplicates_sorted(nums):
    """
    Return the unique values from a sorted list in ascending order.

    Use a read pointer and a write/result position. Do not use a set.

    Example:
    [1, 1, 2, 2, 2, 3] -> [1, 2, 3]
    """
    raise NotImplementedError

def move_zeros_to_end(nums):
    """
    Return a copy with all zeros moved to the end.

    Keep the relative order of all non-zero values.
    Use a slow/write pointer and a fast/read pointer.

    Example:
    [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
    """
    raise NotImplementedError

def sorted_squares(nums):
    """
    Return the squares in ascending order.

    nums is already sorted, but may contain negative values.
    Do not call sort() or sorted() on the result.

    Example:
    [-4, -1, 0, 3, 10] -> [0, 1, 9, 16, 100]
    """
    raise NotImplementedError

def valid_palindrome(text):
    """
    Return True if text is a palindrome after ignoring case and non-letters.

    Move a pointer past characters that should be ignored.

    Example:
    "A man, a plan, a canal: Panama" -> True
    """
    raise NotImplementedError

def has_three_sum_sorted(nums, target):
    """
    Return True if three different positions add up to target.

    nums is sorted. Fix one value, then use two pointers on the remainder.

    Example:
    [1, 2, 3, 4, 7], target 10 -> True because 1 + 2 + 7 = 10
    """
    raise NotImplementedError

def max_water_container(heights):
    """
    Return the maximum water area between two vertical lines.

    Area = distance between pointers * shorter height.
    Move the pointer at the shorter line.

    Example:
    [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49
    """
    raise NotImplementedError
