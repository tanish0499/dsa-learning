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
    reverse = [0] * len(values)
    left = 0
    right = len(values) - 1
    if len(values) == 1:
        return values
    while(left <= right):
        reverse[right] = values[left]
        reverse[left] = values[right]
        left += 1
        right -= 1
    return reverse

def is_palindrome(text):
    """
    Return True if text reads the same forward and backward.

    Compare characters using left and right pointers.

    Example:
    "level" -> True
    "python" -> False
    """
    left = 0
    right = len(text) -1
    while( left < right):
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def pair_sum_sorted(nums, target):
    """
    Return True if two different positions add up to target.

    nums is sorted in ascending order.

    Example:
    [1, 2, 4, 7, 9], target 11 -> True because 2 + 9 = 11
    """
    left = 0
    right = len(nums) - 1
    while(left < right):
        total = nums[left] + nums[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False


def merge_sorted_lists(first, second):
    """
    Merge two sorted lists and return one sorted list.

    Use one pointer for each input list. Do not call sort() or sorted().

    Example:
    [1, 4, 7], [2, 3, 8] -> [1, 2, 3, 4, 7, 8]
    """
    newlist = []
    left = 0
    right = 0
    while left < len(first) and right < len(second):
        if(first[left] <= second[right]):
            newlist.append(first[left])
            left += 1
        else:
            newlist.append(second[right])
            right += 1
    if left < len(first):
        newlist.extend(first[left: len(first)])
    if right < len(second):
        newlist.extend(second[right: len(second)])
    return newlist


def remove_duplicates_sorted(nums):
    """
    Return the unique values from a sorted list in ascending order.

    Use a read pointer and a write/result position. Do not use a set.

    Example:
    [1, 1, 2, 2, 2, 3] -> [1, 2, 3]
    """
    unique = []
    faster = 0
    slower = -1
    if (len(nums) == 0):
        return []
    while faster < len(nums):
        if slower < 0 or nums[faster] != nums[slower]:
            unique.append(nums[faster])
            slower = faster
        faster +=1
    return unique
    raise NotImplementedError


def move_zeros_to_end(nums):
    """
    Return a copy with all zeros moved to the end.

    Keep the relative order of all non-zero values.
    Use a slow/write pointer and a fast/read pointer.

    Example:
    [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
    """
    newlist = []
    read = 0
    # write = -1
    count = 0
    while(read < len(nums)):
        if(nums[read] != 0):
            newlist.append(nums[read])
            write = read
        else:
            count += 1
        read += 1
    if count > 0:
        newlist.extend([0] * count)
    return newlist
    raise NotImplementedError


def sorted_squares(nums):
    """
    Return the squares in ascending order.

    nums is already sorted, but may contain negative values.
    Do not call sort() or sorted() on the result.

    Example:
    [-4, -1, 0, 3, 10] -> [0, 1, 9, 16, 100]
    """
    left = 0
    right = len(nums) - 1
    write = len(nums) - 1
    result = [0] * len(nums)

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[write] = nums[left] * nums[left]
            left += 1
        else:
            result[write] = nums[right] * nums[right]
            right -= 1
        write -= 1
    
    return result
    raise NotImplementedError


def valid_palindrome(text):
    """
    Return True if text is a palindrome after ignoring case and non-letters.

    Move a pointer past characters that should be ignored.

    Example:
    "A man, a plan, a canal: Panama" -> True
    """
    left = 0
    right = len(text) - 1
    while (left < right):
        if not text[left].isalpha():
            left += 1
            continue
        if not text[right].isalpha():
            right -= 1
            continue
        if text[left].casefold() != text[right].casefold():
            return False
        left += 1
        right -= 1
    return True
    raise NotImplementedError


def has_three_sum_sorted(nums, target):
    """
    Return True if three different positions add up to target.

    nums is sorted. Fix one value, then use two pointers on the remainder.

    Example:
    [1, 2, 3, 4, 7], target 10 -> True because 1 + 2 + 7 = 10
    """
    for i in range(len(nums)-2):  
        remainder = target - nums[i]
        left = i + 1
        right = len(nums) - 1
        while(left < right):
            if remainder == nums[left] + nums[right]:
                return True
            elif remainder > nums[left] + nums[right]:
                left += 1
            else:
                right -= 1
    return False


def max_water_container(heights):
    """
    Return the maximum water area between two vertical lines.

    Area = distance between pointers * shorter height.
    Move the pointer at the shorter line.

    Example:
    [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49
    """
    left = 0
    right = len(heights) - 1
    maxarea = 0
    while( left < right):
        if heights[left] < heights[right]:
            shorter = heights[left]
        else:
            shorter = heights[right]
        area = (right - left) * shorter
        if (maxarea < area):
            maxarea = area
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return maxarea
