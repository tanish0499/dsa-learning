"""
Reference solutions for 01 - Arrays and Strings.

Do not open this first. Try the exercise, trace it, and use this only when
you are truly stuck or after you have solved it.
"""


def sum_numbers(nums):
    total = 0

    for num in nums:
        total += num

    return total


def count_even_numbers(nums):
    count = 0

    for num in nums:
        if num % 2 == 0:
            count += 1

    return count


def find_maximum(nums):
    best = nums[0]

    for num in nums:
        if num > best:
            best = num

    return best


def contains_value(nums, target):
    for num in nums:
        if num == target:
            return True

    return False


def double_numbers(nums):
    result = []

    for num in nums:
        result.append(num * 2)

    return result


def count_character(text, target):
    count = 0

    for ch in text:
        if ch == target:
            count += 1

    return count


def reverse_string(text):
    result = []

    for i in range(len(text) - 1, -1, -1):
        result.append(text[i])

    return "".join(result)


def only_positive_numbers(nums):
    result = []

    for num in nums:
        if num > 0:
            result.append(num)

    return result


def second_largest(nums):
    largest = None
    second = None

    for num in nums:
        if num == largest or num == second:
            continue

        if largest is None or num > largest:
            second = largest
            largest = num
        elif second is None or num > second:
            second = num

    return second


def move_zeroes_to_end(nums):
    result = []
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)

    for _ in range(zero_count):
        result.append(0)

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


def compress_repeated_chars(text):
    if text == "":
        return ""

    result = []
    current = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current:
            count += 1
        else:
            result.append(current + str(count))
            current = text[i]
            count = 1

    result.append(current + str(count))
    return "".join(result)

