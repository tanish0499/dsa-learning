"""Reviewed reference solutions for the mixed-foundations checkpoint."""


def common_unique_values(first, second):
    values_in_second = set(second)
    emitted = set()
    result = []

    for value in first:
        if value in values_in_second and value not in emitted:
            emitted.add(value)
            result.append(value)

    return result


def is_subsequence(candidate, text):
    candidate_index = 0

    for char in text:
        if candidate_index < len(candidate) and char == candidate[candidate_index]:
            candidate_index += 1

    return candidate_index == len(candidate)


def first_nearby_repeat(nums, k):
    if k <= 0:
        return None

    left = 0
    window = set()

    for right in range(len(nums)):
        current = nums[right]
        if current in window:
            return current

        window.add(current)

        if right - left + 1 > k:
            window.remove(nums[left])
            left += 1

    return None


def pair_with_difference_sorted(nums, difference):
    slow = 0
    fast = 1

    while fast < len(nums):
        if slow == fast:
            fast += 1
            continue

        current_difference = nums[fast] - nums[slow]

        if current_difference == difference:
            return True
        if current_difference < difference:
            fast += 1
        else:
            slow += 1

    return False


def count_distinct_windows(text, k):
    if k <= 0 or k > len(text):
        return 0

    left = 0
    counts = {}
    result = 0

    for right in range(len(text)):
        incoming = text[right]
        counts[incoming] = counts.get(incoming, 0) + 1

        if right - left + 1 > k:
            outgoing = text[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1

        if right - left + 1 == k and len(counts) == k:
            result += 1

    return result


def maximum_sum_distinct_window(nums, k):
    if k <= 0 or k > len(nums):
        return None

    left = 0
    counts = {}
    window_sum = 0
    largest_sum = None

    for right in range(len(nums)):
        incoming = nums[right]
        window_sum += incoming
        counts[incoming] = counts.get(incoming, 0) + 1

        if right - left + 1 > k:
            outgoing = nums[left]
            window_sum -= outgoing
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1

        if right - left + 1 == k and len(counts) == k:
            if largest_sum is None or window_sum > largest_sum:
                largest_sum = window_sum

    return largest_sum


def longest_subarray_at_most_k_distinct(nums, k):
    if k <= 0:
        return 0

    left = 0
    counts = {}
    longest = 0

    for right in range(len(nums)):
        incoming = nums[right]
        counts[incoming] = counts.get(incoming, 0) + 1

        while len(counts) > k:
            outgoing = nums[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1

        longest = max(longest, right - left + 1)

    return longest


def shortest_window_containing_required_brute_force(nums, required):
    required_values = set(required)

    if not required_values:
        return 0

    smallest = None

    for left in range(len(nums)):
        found = set()

        for right in range(left, len(nums)):
            if nums[right] in required_values:
                found.add(nums[right])

            if len(found) == len(required_values):
                window_size = right - left + 1
                if smallest is None or window_size < smallest:
                    smallest = window_size
                break

    return 0 if smallest is None else smallest


def shortest_window_containing_required(nums, required):
    required_values = set(required)

    if not required_values:
        return 0

    left = 0
    counts = {}
    smallest = None

    for right in range(len(nums)):
        incoming = nums[right]
        if incoming in required_values:
            counts[incoming] = counts.get(incoming, 0) + 1

        while len(counts) == len(required_values):
            window_size = right - left + 1
            if smallest is None or window_size < smallest:
                smallest = window_size

            outgoing = nums[left]
            if outgoing in required_values:
                counts[outgoing] -= 1
                if counts[outgoing] == 0:
                    del counts[outgoing]
            left += 1

    return 0 if smallest is None else smallest


def closest_pair_sum_sorted_brute_force(nums, target):
    closest_sum = None
    closest_distance = None

    for first in range(len(nums) - 1):
        for second in range(first + 1, len(nums)):
            current_sum = nums[first] + nums[second]
            current_distance = abs(target - current_sum)

            if (
                closest_distance is None
                or current_distance < closest_distance
                or (
                    current_distance == closest_distance
                    and current_sum < closest_sum
                )
            ):
                closest_distance = current_distance
                closest_sum = current_sum

    return closest_sum


def closest_pair_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    closest_sum = None
    closest_distance = None

    while left < right:
        current_sum = nums[left] + nums[right]
        current_distance = abs(target - current_sum)

        if (
            closest_distance is None
            or current_distance < closest_distance
            or (
                current_distance == closest_distance
                and current_sum < closest_sum
            )
        ):
            closest_distance = current_distance
            closest_sum = current_sum

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return target

    return closest_sum


def longest_consecutive_run(nums):
    values = set(nums)
    longest = 0

    for value in values:
        if value - 1 not in values:
            current = value
            run_length = 1

            while current + 1 in values:
                current += 1
                run_length += 1

            longest = max(longest, run_length)

    return longest
