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
    unique = set ()
    total = []
    for num in second:
        if num not in unique:
            unique.add(num)
    for num in first:
        if num in unique and num not in total:
            total.append(num)
    return total


def is_subsequence(candidate, text):
    """
    Return True if candidate can be made by deleting characters from text
    without changing the order of the remaining characters.

    Example:
    candidate="ace", text="abcde" -> True
    candidate="aec", text="abcde" -> False
    """
    left = 0
    right = 0
    while left < len(candidate) and right < len(text):
        if candidate[left] == text[right]:
            left += 1
        right += 1
    if left == len(candidate):
        return True
    return False

def first_nearby_repeat(nums, k):
    """
    Return the first value encountered whose previous equal value is at most k
    indices behind it. Return None if no such value exists.

    Example:
    [5, 1, 2, 1, 5], k=2 -> 1
    """
    left = 0
    window = set ()
    for right in range(len(nums)):
        if nums[right] in window:
            return nums[right]
        window.add(nums[right])
        if right - left + 1 > k:
            window.discard(nums[left])
            left += 1
    return None


def pair_with_difference_sorted(nums, difference):
    """
    Return True if two different positions have the given difference.

    nums is sorted in ascending order and difference is non-negative.

    Example:
    [1, 3, 5, 8], difference=3 -> True because 8 - 5 = 3
    """
    # left = 0
    # remain = 0
    # for right in range(len(nums)):
    #     remain = nums[right] - remain
    #     if right - left + 1 > 2:
    #         remain = remain - nums[left]
    #         left += 1
    #     if remain == difference:
    #         return True
    # return False
    fast = 1
    slow = 0
    while fast < len(nums):
        if fast == slow:
            fast += 1
            continue
        remain = nums[fast] - nums[slow]
        if difference == remain:
            return True
        elif difference > remain:
            fast += 1
        else:
            slow += 1
    return False

def count_distinct_windows(text, k):
    """
    Return the number of length-k substrings containing no repeated character.

    Return 0 when k <= 0 or k is larger than text.

    Example:
    text="abac", k=3 -> 1 because only "bac" has distinct characters
    """
    if k <= 0 or k > len(text):
        return 0
    left = 0
    counts = {}
    distinct_window_count = 0
    for right in range(len(text)):
        incoming = text[right]
        if incoming not in counts:
            counts[incoming] = 0
        counts[incoming] += 1
        if right - left + 1 > k:
            outgoing = text[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1
        if right - left + 1 == k and len(counts) == k:
            distinct_window_count += 1
    return distinct_window_count

def maximum_sum_distinct_window(nums, k):
    """
    Return the largest sum of a length-k window whose values are all distinct.

    Return None when k <= 0, k is larger than nums, or no window qualifies.

    Example:
    [1, 5, 4, 2, 9, 9, 9], k=3 -> 15 from [4, 2, 9]
    """
    if k <= 0 or k > len(nums):
        return None
    left = 0
    counts = {}
    largest = None
    window_sum = 0
    for right in range(len(nums)):
        incoming = nums[right]
        window_sum += incoming
        if incoming not in counts:
            counts[incoming] = 0
        counts[incoming] += 1
        if right - left + 1 > k:
            outgoing = nums[left]
            window_sum -= outgoing
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1
        if right - left + 1 == k and len(counts) == k:
            total_sum = sum(counts)
            if largest is None or largest < total_sum:
                largest = total_sum
    return largest


def longest_subarray_at_most_k_distinct(nums, k):
    """
    Return the longest continuous length containing at most k distinct values.

    Return 0 when k <= 0.

    Example:
    [1, 2, 1, 2, 3], k=2 -> 4 from [1, 2, 1, 2]
    """
    if k <= 0 or k > len(nums):
        return 0
    left = 0
    counts = {}
    longest = 0
    for right in range(len(nums)):
        incoming = nums[right]
        if incoming not in counts:
            counts[incoming] = 0
        counts[incoming] += 1
        while len(counts) > k:
            outgoing = nums[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1
        if len(counts) <= k:
            each_window_max = sum(counts.values())
            if longest < each_window_max:
                longest = each_window_max
    return longest

def shortest_window_containing_required(nums, required):
    """
    Return the smallest continuous length containing every distinct value in
    required at least once. Return 0 if no window qualifies or required is empty.

    Example:
    nums=[1, 2, 2, 3, 1, 2], required=[1, 3] -> 2 from [3, 1]
    """
    if len(required) == 0:
        return 0
    counts = {}
    required_set = set(required)
    left = 0
    min_length = None
    for right in range(len(nums)):
        incoming = nums[right]
        if incoming in required_set:
            if incoming not in counts:
                counts[incoming] = 0
            counts[incoming] += 1
        while len(required_set) == len(counts):
            windows_size = right - left + 1
            if min_length is None or min_length > windows_size:
                min_length = windows_size
            outgoing = nums[left]
            if outgoing in required_set:
                counts[outgoing] -= 1
                if counts[outgoing] == 0:
                    del counts[outgoing]
            left += 1
    if min_length is None:
        min_length = 0
    return min_length

def closest_pair_sum_sorted(nums, target):
    """
    Return the sum of two different positions that is closest to target.

    nums is sorted. Return None when fewer than two values exist. If two sums
    are equally close, return the smaller sum.

    Example:
    [1, 3, 4, 7, 10], target=15 -> 14 from 4 + 10
    """
    min_total = None
    min_sub = None
    p1 = 0
    p2 = len(nums) -1
    while p1 < p2:
        current_sum = nums[p1] + nums[p2]
        remainder = abs(target - current_sum)
        if (min_sub is None or min_sub > remainder) or (min_sub == remainder and current_sum < min_total):
            min_sub = remainder
            min_total = current_sum
        if current_sum < target:
            p1 += 1
        elif current_sum > target:
            p2 -= 1
        else:
            return target
    return min_total
    
    # min_sub = None
    # min_i = 0
    # min_j = 0
    # closest_sum = None
    # min_total = None
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         total = nums[i] + nums[j]
    #         remainder = abs(target - total)
    #         if (min_sub is None or min_sub > remainder) or (min_sub == remainder and total < min_total):
    #             min_sub = remainder
    #             min_total = total
    #             min_i = i
    #             min_j = j
    # return min_total
        
    


    raise NotImplementedError


def longest_consecutive_run(nums):
    """
    Return the length of the longest run of consecutive integer values.

    Input order does not matter and repeated values count once. Aim for O(n)
    time without calling sort() or sorted().

    Example:
    [100, 4, 200, 1, 3, 2] -> 4 from 1, 2, 3, 4
    """
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            count = 1
            while current + 1 in num_set:
                count += 1
                current += 1
            if longest < count:
                longest = count
    return longest