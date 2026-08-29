"""
Arrays and strings exercises.

Implement one function at a time, then run:

python -m unittest discover -s exercises/python
"""


def sum_numbers(nums):
    """Return the sum of all numbers in nums."""
    sum = 0
    for num in nums:
        sum = sum + num
    return sum
    raise NotImplementedError


def count_even_numbers(nums):
    """Return how many numbers in nums are even."""
    count=0
    for num in nums:
        if(num%2==0):
            count+=1
    return count
    raise NotImplementedError


def find_maximum(nums):
    """Return the largest number in nums. nums will not be empty."""
    best=nums[0]
    for num in nums:
        if(num>best):
            best = num
    return best
    raise NotImplementedError


def contains_value(nums, target):
    """Return True if target exists in nums, otherwise False."""
    for num in nums:
        if(target == num):
            return True
    return False
    raise NotImplementedError


def double_numbers(nums):
    """Return a new list where every number is doubled."""
    nums2=[]
    for num in nums:
        nums2.append(num * 2)
    return nums2
    raise NotImplementedError


def count_character(text, target):
    """Return how many times target appears in text."""
    count = 0
    for char in text:
        if(char==target):
            count+=1
    return count
    raise NotImplementedError


def reverse_string(text):
    """Return text reversed."""
    revchars=[]
    for i in range(len(text)-1, -1, -1):
        revchars.append(text[i])
    return "".join(revchars)

    raise NotImplementedError


def only_positive_numbers(nums):
    """Return a new list containing only numbers greater than 0."""
    even = []
    for num in nums:
        if(num > 0):
            even.append(num)
    return even
    raise NotImplementedError


def second_largest(nums):
    """
    Return the second largest distinct number.
    Example:
    [4, 1, 9, 9, 2] -> 4

    nums will contain at least two distinct numbers.
    """

    unique = []
    for i in range(0, len(nums)):
        isUnique=True
        for j in range(0,i):
            if(nums[i] == nums[j]):
                isUnique = False
                break
            j +=1
        if(isUnique):
            unique.append(nums[i])
        i +=1
    biggest =unique[0]
    secondBig = None
    for i in range(1, len(unique)):
        if unique[i] > biggest:
            secondBig = biggest
            biggest = unique[i]
        elif(secondBig is None or unique[i] > secondBig):
            secondBig = unique[i]
        i += 1
    return secondBig
    raise NotImplementedError


def move_zeroes_to_end(nums):
    """
    Return a new list with all zeroes moved to the end.

    Keep the order of non-zero numbers.

    Example:
    [0, 3, 0, 1, 5] -> [3, 1, 5, 0, 0]
    """
    new = []
    count = 0
    for num in nums:
        if(num == 0):
            count +=1
        else:
            new.append(num)
    
    for i in range(count):
        new.append(0)
    
    return new
    raise NotImplementedError


def is_palindrome(text):
    """
    Return True if text reads the same forward and backward.

    For now, treat the text exactly as given.
    Example:
    "level" -> True
    "Level" -> False
    """
    isPalindrom = True
    for i in range(0, len(text)):
        if(text[i] != text[len(text)-1-i]):
            isPalindrom = False
            break
    return isPalindrom
    raise NotImplementedError


def compress_repeated_chars(text):
    """
    Compress consecutive repeated characters.

    Examples:
    "aaabbc" -> "a3b2c1"
    "x" -> "x1"
    "" -> ""
    """
    count = 0
    if(len(text) == 0):
        return ""
    unique = text[0]
    new = []
    for i in range(0, len(text)):
        if(text[i] == unique):
            count += 1
        else:
            new.append(unique)
            new.append(count)
            unique = text[i]
            count=1
    new.append(unique + str(count))
    return "".join(map(str,new))
        
    raise NotImplementedError

