"""Reviewed reference solutions for sliding-window exercises."""


def fixed_window_sums(nums, k):
    if k <= 0 or k > len(nums):
        return []

    left = 0
    window_sum = 0
    result = []

    for right in range(len(nums)):
        window_sum += nums[right]

        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        if right - left + 1 == k:
            result.append(window_sum)

    return result


def max_sum_fixed_window(nums, k):
    if k <= 0 or k > len(nums):
        return None

    left = 0
    window_sum = 0
    largest_sum = None

    for right in range(len(nums)):
        window_sum += nums[right]

        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        if right - left + 1 == k:
            if largest_sum is None or window_sum > largest_sum:
                largest_sum = window_sum

    return largest_sum


def count_windows_at_least(nums, k, threshold):
    if k <= 0 or k > len(nums):
        return 0

    left = 0
    window_sum = 0
    qualifying_count = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        if right - left + 1 == k and window_sum >= threshold:
            qualifying_count += 1

    return qualifying_count


def max_vowels_in_window(text, k):
    if k <= 0 or k > len(text):
        return 0

    vowels = {"a", "e", "i", "o", "u"}
    left = 0
    current_count = 0
    largest_count = 0

    for right in range(len(text)):
        if text[right].casefold() in vowels:
            current_count += 1

        if right - left + 1 > k:
            if text[left].casefold() in vowels:
                current_count -= 1
            left += 1

        if right - left + 1 == k:
            largest_count = max(largest_count, current_count)

    return largest_count


def has_nearby_duplicate(nums, k):
    if k <= 0:
        return False

    left = 0
    window = set()

    for right in range(len(nums)):
        if nums[right] in window:
            return True

        window.add(nums[right])

        if right - left + 1 > k:
            window.remove(nums[left])
            left += 1

    return False


def smallest_subarray_at_least(nums, target):
    left = 0
    window_sum = 0
    smallest = None

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            window_size = right - left + 1
            if smallest is None or window_size < smallest:
                smallest = window_size

            window_sum -= nums[left]
            left += 1

    return 0 if smallest is None else smallest


def longest_subarray_at_most(nums, limit):
    if limit < 0:
        return 0

    left = 0
    window_sum = 0
    longest = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > limit:
            window_sum -= nums[left]
            left += 1

        longest = max(longest, right - left + 1)

    return longest


def longest_unique_substring(text):
    left = 0
    window = set()
    longest = 0

    for right in range(len(text)):
        while text[right] in window:
            window.remove(text[left])
            left += 1

        window.add(text[right])
        longest = max(longest, right - left + 1)

    return longest


def find_anagram_indices(text, pattern):
    if not pattern or len(pattern) > len(text):
        return []

    pattern_counts = {}
    window_counts = {}

    for char in pattern:
        pattern_counts[char] = pattern_counts.get(char, 0) + 1

    left = 0
    result = []

    for right in range(len(text)):
        incoming = text[right]
        window_counts[incoming] = window_counts.get(incoming, 0) + 1

        if right - left + 1 > len(pattern):
            outgoing = text[left]
            window_counts[outgoing] -= 1
            if window_counts[outgoing] == 0:
                del window_counts[outgoing]
            left += 1

        if window_counts == pattern_counts:
            result.append(left)

    return result


def longest_repeating_after_replacements(text, k):
    if k < 0:
        return 0

    left = 0
    counts = {}
    highest_frequency = 0
    longest = 0

    for right in range(len(text)):
        incoming = text[right]
        counts[incoming] = counts.get(incoming, 0) + 1
        highest_frequency = max(highest_frequency, counts[incoming])

        while right - left + 1 - highest_frequency > k:
            outgoing = text[left]
            counts[outgoing] -= 1
            left += 1

        longest = max(longest, right - left + 1)

    return longest
