"""Reviewed reference solutions for hash map and set exercises."""


def has_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


def count_values(values):
    counts = {}

    for value in values:
        counts[value] = counts.get(value, 0) + 1

    return counts


def count_characters(text):
    counts = {}

    for char in text:
        counts[char] = counts.get(char, 0) + 1

    return counts


def first_repeated_value(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return None


def unique_values(values):
    seen = set()
    result = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


def most_frequent_value(values):
    counts = {}
    most_frequent = None
    highest_count = 0

    for value in values:
        counts[value] = counts.get(value, 0) + 1

        if counts[value] > highest_count:
            highest_count = counts[value]
            most_frequent = value

    return most_frequent


def two_sum(nums, target):
    seen = set()

    for num in nums:
        needed = target - num
        if needed in seen:
            return True
        seen.add(num)

    return False


def is_anagram(first, second):
    if len(first) != len(second):
        return False

    first_counts = count_characters(first)
    second_counts = count_characters(second)

    for char, count in first_counts.items():
        if second_counts.get(char) != count:
            return False

    return True


def group_words_by_first_letter(words):
    groups = {}

    for word in words:
        first_letter = word[0]
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(word)

    return groups


def first_non_repeating_character(text):
    counts = count_characters(text)

    for char in text:
        if counts[char] == 1:
            return char

    return None
