"""
Hash maps and sets exercises.

Implement one function at a time, then run:

python -m unittest discover -s exercises/python
"""


def has_duplicate(nums):
    """Return True if any number appears more than once."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def count_values(values):
    """
    Return a dictionary counting how many times each value appears.

    Example:
    ["dev", "ops", "dev"] -> {"dev": 2, "ops": 1}
    """
    counts = {}
    for value in values:
        if value not in counts:
            counts[value] = 0
        counts[value] += 1
    return counts


def count_characters(text):
    """
    Return a dictionary counting how many times each character appears.

    Example:
    "hello" -> {"h": 1, "e": 1, "l": 2, "o": 1}
    """
    dictionary = {}
    for char in text:
        if char not in dictionary:
            dictionary[char] = 0
        dictionary[char] += 1

    return dictionary


def first_repeated_value(nums):
    """
    Return the first value that appears for a second time.

    Example:
    [5, 1, 3, 1, 5] -> 1

    Return None if there is no repeated value.
    """
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return num
    return None


def unique_values(values):
    """
    Return a list containing each value once, keeping first-seen order.

    Example:
    ["a", "b", "a", "c", "b"] -> ["a", "b", "c"]
    """
    seen = set()
    unique = []
    for char in values:
        if char not in seen:
            seen.add(char)
            unique.append(char)
    return unique


def most_frequent_value(values):
    """
    Return the value that appears most often.

    If there is a tie, return the value that reached that frequency first.
    values will not be empty.

    Example:
    ["a", "b", "a", "c"] -> "a"
    """
    dictionary = {}
    highest = 0
    highchar = None
    for char in values:
        if char not in dictionary:
            dictionary[char] = 0
        dictionary[char] += 1
        if dictionary[char] > highest:
            highest = dictionary[char]
            highchar = char

    return highchar
    raise NotImplementedError


def two_sum(nums, target):
    """
    Return True if two different numbers in nums add up to target.

    Example:
    nums = [4, 2, 7, 1], target = 9 -> True because 2 + 7 = 9
    """
    seen = set()
    for num in nums:
        needed = target - num
        if needed in seen:
            return True
        seen.add(num)
    return False
    raise NotImplementedError


def is_anagram(first, second):
    """
    Return True if first and second use the same characters with the same counts.

    Example:
    "listen", "silent" -> True
    "apple", "papel" -> True
    "rat", "car" -> False
    """
    if len(first) != len(second):
        return False
    dictionary1 = {}
    dictionary2 = {}
    for char in first:
        if char not in dictionary1:
            dictionary1[char] = 0
        dictionary1[char] += 1
    for char in second:
        if char not in dictionary2:
            dictionary2[char] = 0
        dictionary2[char] += 1
    
    # compare dictionary directly
    # return dictionary1 == dictionary2

    # compare dictionary using for loop
    for char,count in dictionary1.items():
        if char not in dictionary2:
            return False
        if dictionary1[char] != dictionary2[char]:
            return False
    
    return True


def group_words_by_first_letter(words):
    """
    Return a dictionary grouping words by their first letter.

    Example:
    ["dev", "dog", "ops"] -> {"d": ["dev", "dog"], "o": ["ops"]}

    words will not contain empty strings.
    """
    dictionary = {}
    for word in words:
        if word[0] not in dictionary:
            dictionary[word[0]] = []
        dictionary[word[0]].append(word)
    return dictionary
    raise NotImplementedError


def first_non_repeating_character(text):
    """
    Return the first character that appears exactly once.

    Example:
    "swiss" -> "w"

    Return None if every character repeats.
    """
    dictionary = {}
    for char in text:
        if char not in dictionary:
            dictionary[char] = 0
        dictionary[char] += 1
    
    for char, count in dictionary.items():
        if count == 1:
            return char
    return None
