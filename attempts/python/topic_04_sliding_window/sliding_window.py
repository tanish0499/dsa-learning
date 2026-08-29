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
    left = 0
    total = []
    window_sum = 0
    if k <= 0 or k > len(nums):
        return []
    for right in range(len(nums)):
        window_sum = nums[right] + window_sum
        if right - left + 1 > k:
            window_sum = window_sum - nums[left]
            left += 1
        if right - left + 1 == k:
            total.append(window_sum)
    return total


def max_sum_fixed_window(nums, k):
    """
    Return the largest sum among all continuous windows of size k.

    Return None when k <= 0 or k is larger than nums.
    Do not recalculate each complete window from scratch.

    Example:
    [2, 1, 5, 1, 3, 2], k=3 -> 9
    """
    max_sum = None
    window_sum = 0
    left = 0
    if k <= 0 or len(nums) < k:
        return None
    for right in range(len(nums)):
        window_sum = window_sum + nums[right]
        if right - left + 1 > k:
            window_sum = window_sum - nums[left]
            left += 1
        if right - left + 1 == k:
            if max_sum is None or window_sum > max_sum:
                max_sum = window_sum
    return max_sum
    raise NotImplementedError


def count_windows_at_least(nums, k, threshold):
    """
    Return how many size-k windows have a sum at least threshold.

    Return 0 when k <= 0 or k is larger than nums.

    Example:
    [2, 1, 5, 1, 3, 2], k=3, threshold=8 -> 2
    """
    left = 0
    sum = 0
    threshold_count = 0
    if k <= 0 or k > len(nums):
        return 0
    for right in range(len(nums)):
        sum = sum + nums[right]
        if right - left + 1 > k:
            sum = sum - nums[left]
            left += 1
        if right - left + 1 == k:
            if sum >= threshold:
                threshold_count += 1
    return threshold_count


def max_vowels_in_window(text, k):
    """
    Return the largest number of vowels in any substring of length k.

    Treat a, e, i, o, and u as vowels and ignore case.
    Return 0 when k <= 0 or k is larger than text.

    Example:
    "abciiidef", k=3 -> 3
    """
    left = 0
    vowels = ['a','e','i','o','u']
    total_vowels = 0
    max_vowels = 0
    if k <= 0 or k > len(text):
        return 0
    for right in range(len(text)):
        if text[right].casefold() in vowels:
            total_vowels += 1
        if right - left + 1 > k:
            if text[left].casefold() in vowels:
                total_vowels -= 1
            left += 1
        if right - left + 1 == k:
            if max_vowels < total_vowels:
                max_vowels = total_vowels
    return max_vowels

def has_nearby_duplicate(nums, k):
    """
    Return True if equal values occur at indices at most k apart.

    Keep a set representing the most recent k values.

    Example:
    [1, 2, 3, 1], k=3 -> True
    [1, 2, 3, 1], k=2 -> False
    """
    left = 0
    window = set()
    for right in range(len(nums)):
        if nums[right] in window:
            return True
        window.add(nums[right])
        if right - left + 1 > k:
            window.discard(nums[left])
            left += 1
    return False


def smallest_subarray_at_least(nums, target):
    """
    Return the smallest length whose continuous sum is at least target.

    nums contains only positive integers. Return 0 if no window qualifies.

    Example:
    [2, 3, 1, 2, 4, 3], target=7 -> 2 because [4, 3]
    """
    left = 0
    window_sum = 0
    smallest_window_size = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            window_size = right - left + 1
            if smallest_window_size == 0:
                smallest_window_size = window_size
            if smallest_window_size > window_size:
                smallest_window_size = window_size
            window_sum -= nums[left]
            left += 1
    return smallest_window_size


def longest_subarray_at_most(nums, limit):
    """
    Return the longest length whose continuous sum is at most limit.

    nums contains only non-negative integers.

    Example:
    [2, 1, 4, 1, 1], limit=7 -> 4 because [1, 4, 1, 1] sums to 7
    """
    left = 0
    window_sum  = 0
    largest_window_size = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > limit:
            window_sum -= nums[left]
            left += 1
        window_size = right - left + 1
        if largest_window_size == 0 or largest_window_size < window_size:
            largest_window_size = window_size
    return largest_window_size


def longest_unique_substring(text):
    """
    Return the length of the longest substring without repeated characters.

    Example:
    "abcabcbb" -> 3 because "abc" has no repeats
    """
    left = 0
    unique = set()
    longest = 0
    for right in range(len(text)):
        while text[right] in unique:
            unique.discard(text[left])
            left += 1
        unique.add(text[right])
        window_size = right - left + 1
        if longest < window_size:
            longest = window_size
    return longest
    raise NotImplementedError


def find_anagram_indices(text, pattern):
    """
    Return start indices where an anagram of pattern occurs in text.

    Example:
    text="cbaebabacd", pattern="abc" -> [0, 6]
    """
    left = 0
    # unique = set()
    # total = []
    # pattern_set = set(pattern)
    # for right in range(len(text)):
    #     unique.add(text[right])
    #     if right - left + 1 > len(pattern_set):
    #         unique.discard(text[left])
    #         left += 1
    #     if pattern_set == unique:
    #         total.append(left)
    # return total

    dict1 = {}
    dict2 = {}
    k = len(pattern)
    count = []

    if len(pattern) == 0 or len(text) < len(pattern):
        return []
    for ch in pattern:
        if ch not in dict2:
            dict2[ch] = 0
        dict2[ch] += 1
    for right in range(len(text)):
        if text[right] not in dict1:
            dict1[text[right]] = 0
        dict1[text[right]] += 1
        if right - left + 1 > k:
            dict1[text[left]] -= 1
            if dict1[text[left]] == 0:
                del dict1[text[left]]
            left += 1
        if right - left + 1 == k and dict1 == dict2:
            count.append(left)
    return count

def longest_repeating_after_replacements(text, k):
    """
    Return the longest substring that can become one repeated character after
    replacing at most k characters.

    Example:
    text="AABBABBA", k=1 -> 4
    """
    left = 0
    dictionary = {}
    longest = 0
    if k < 0:
        return 0
    for right in range(len(text)):
        if text[right] not in dictionary:
            dictionary[text[right]] = 0
        dictionary[text[right]] += 1
        while right - left + 1  - max(dictionary.values()) > k:
            dictionary[text[left]] -= 1
            if dictionary[text[left]] == 0:
                del dictionary[text[left]]
            left += 1
        if longest < sum(dictionary.values()):
            longest = sum(dictionary.values())
    return longest               
    raise NotImplementedError
