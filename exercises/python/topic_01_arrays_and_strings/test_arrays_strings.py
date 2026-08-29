import os
import unittest

if os.getenv("DSA_TEST_TARGET") == "solutions":
    from solutions.python.topic_01_arrays_and_strings.arrays_strings_solutions import (
        compress_repeated_chars,
        contains_value,
        count_character,
        count_even_numbers,
        double_numbers,
        find_maximum,
        is_palindrome,
        move_zeroes_to_end,
        only_positive_numbers,
        reverse_string,
        second_largest,
        sum_numbers,
    )
else:
    from .arrays_strings import (
    compress_repeated_chars,
    contains_value,
    count_character,
    count_even_numbers,
    double_numbers,
    find_maximum,
    is_palindrome,
    move_zeroes_to_end,
    only_positive_numbers,
    reverse_string,
    second_largest,
    sum_numbers,
    )


class TestArraysAndStrings(unittest.TestCase):
    def assert_function_returns(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")

        self.assertEqual(actual, expected)

    def test_sum_numbers(self):
        self.assert_function_returns(sum_numbers, ([1, 2, 3],), 6)
        self.assert_function_returns(sum_numbers, ([],), 0)
        self.assert_function_returns(sum_numbers, ([-2, 5, 10],), 13)

    def test_count_even_numbers(self):
        self.assert_function_returns(count_even_numbers, ([2, 5, 8, 9],), 2)
        self.assert_function_returns(count_even_numbers, ([1, 3, 5],), 0)
        self.assert_function_returns(count_even_numbers, ([],), 0)

    def test_find_maximum(self):
        self.assert_function_returns(find_maximum, ([4, 1, 9, 2],), 9)
        self.assert_function_returns(find_maximum, ([-10, -3, -7],), -3)
        self.assert_function_returns(find_maximum, ([5],), 5)

    def test_contains_value(self):
        self.assert_function_returns(contains_value, ([1, 2, 3], 2), True)
        self.assert_function_returns(contains_value, ([1, 2, 3], 9), False)
        self.assert_function_returns(contains_value, ([], 1), False)

    def test_double_numbers(self):
        self.assert_function_returns(double_numbers, ([1, 2, 3],), [2, 4, 6])
        self.assert_function_returns(double_numbers, ([],), [])
        self.assert_function_returns(double_numbers, ([-1, 5],), [-2, 10])

    def test_count_character(self):
        self.assert_function_returns(count_character, ("hello", "l"), 2)
        self.assert_function_returns(count_character, ("devops", "z"), 0)
        self.assert_function_returns(count_character, ("", "a"), 0)

    def test_reverse_string(self):
        self.assert_function_returns(reverse_string, ("abc",), "cba")
        self.assert_function_returns(reverse_string, ("a",), "a")
        self.assert_function_returns(reverse_string, ("",), "")

    def test_only_positive_numbers(self):
        self.assert_function_returns(only_positive_numbers, ([-1, 0, 2, 5],), [2, 5])
        self.assert_function_returns(only_positive_numbers, ([-3, -1, 0],), [])
        self.assert_function_returns(only_positive_numbers, ([],), [])

    def test_second_largest(self):
        self.assert_function_returns(second_largest, ([4, 1, 9, 9, 2],), 4)
        self.assert_function_returns(second_largest, ([10, 5],), 5)
        self.assert_function_returns(second_largest, ([-2, -8, -1],), -2)
        self.assert_function_returns(second_largest, ([-1, -2, -3],), -2)

    def test_move_zeroes_to_end(self):
        self.assert_function_returns(
            move_zeroes_to_end,
            ([0, 3, 0, 1, 5],),
            [3, 1, 5, 0, 0],
        )
        self.assert_function_returns(move_zeroes_to_end, ([1, 2, 3],), [1, 2, 3])
        self.assert_function_returns(move_zeroes_to_end, ([0, 0],), [0, 0])

    def test_is_palindrome(self):
        self.assert_function_returns(is_palindrome, ("level",), True)
        self.assert_function_returns(is_palindrome, ("",), True)
        self.assert_function_returns(is_palindrome, ("Level",), False)
        self.assert_function_returns(is_palindrome, ("hello",), False)

    def test_compress_repeated_chars(self):
        self.assert_function_returns(compress_repeated_chars, ("aaabbc",), "a3b2c1")
        self.assert_function_returns(compress_repeated_chars, ("x",), "x1")
        self.assert_function_returns(compress_repeated_chars, ("",), "")


if __name__ == "__main__":
    unittest.main()
