"""Reviewed reference solutions for two-pointer exercises."""


def reverse_values(values):
    result = list(values)
    left = 0
    right = len(result) - 1

    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    return result


def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


def pair_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return False


def merge_sorted_lists(first, second):
    first_index = 0
    second_index = 0
    merged = []

    while first_index < len(first) and second_index < len(second):
        if first[first_index] <= second[second_index]:
            merged.append(first[first_index])
            first_index += 1
        else:
            merged.append(second[second_index])
            second_index += 1

    merged.extend(first[first_index:])
    merged.extend(second[second_index:])
    return merged


def remove_duplicates_sorted(nums):
    if not nums:
        return []

    result = [nums[0]]

    for read in range(1, len(nums)):
        if nums[read] != result[-1]:
            result.append(nums[read])

    return result


def move_zeros_to_end(nums):
    result = [0] * len(nums)
    write = 0

    for value in nums:
        if value != 0:
            result[write] = value
            write += 1

    return result


def sorted_squares(nums):
    result = [0] * len(nums)
    left = 0
    right = len(nums) - 1

    for write in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[write] = nums[left] ** 2
            left += 1
        else:
            result[write] = nums[right] ** 2
            right -= 1

    return result


def valid_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
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


def has_three_sum_sorted(nums, target):
    for first in range(len(nums) - 2):
        left = first + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[first] + nums[left] + nums[right]

            if current_sum == target:
                return True
            if current_sum < target:
                left += 1
            else:
                right -= 1

    return False


def max_water_container(heights):
    left = 0
    right = len(heights) - 1
    largest_area = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        largest_area = max(largest_area, width * height)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return largest_area
