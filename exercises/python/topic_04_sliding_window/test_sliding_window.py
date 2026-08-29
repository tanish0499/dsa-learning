import os
import unittest

if os.getenv("DSA_TEST_TARGET") == "solutions":
    from solutions.python.topic_04_sliding_window.sliding_window_solutions import (
        count_windows_at_least,
        find_anagram_indices,
        fixed_window_sums,
        has_nearby_duplicate,
        longest_repeating_after_replacements,
        longest_subarray_at_most,
        longest_unique_substring,
        max_sum_fixed_window,
        max_vowels_in_window,
        smallest_subarray_at_least,
    )
else:
    from .sliding_window import (
    count_windows_at_least,
    find_anagram_indices,
    fixed_window_sums,
    has_nearby_duplicate,
    longest_repeating_after_replacements,
    longest_subarray_at_most,
    longest_unique_substring,
    max_sum_fixed_window,
    max_vowels_in_window,
    smallest_subarray_at_least,
    )


class TestSlidingWindow(unittest.TestCase):
    def assert_function_returns(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")

        self.assertEqual(actual, expected)

    def test_fixed_window_sums(self):
        self.assert_function_returns(
            fixed_window_sums,
            ([2, 1, 5, 1, 3, 2], 3),
            [8, 7, 9, 6],
        )
        self.assert_function_returns(fixed_window_sums, ([1, 2], 2), [3])
        self.assert_function_returns(fixed_window_sums, ([1, 2], 3), [])
        self.assert_function_returns(fixed_window_sums, ([1, 2], 0), [])
        self.assert_function_returns(fixed_window_sums, ([-1, -2, -3], 2), [-3, -5])

    def test_max_sum_fixed_window(self):
        self.assert_function_returns(max_sum_fixed_window, ([2, 1, 5, 1, 3, 2], 3), 9)
        self.assert_function_returns(max_sum_fixed_window, ([-5, -2, -8], 2), -7)
        self.assert_function_returns(max_sum_fixed_window, ([1, 2], 3), None)

    def test_count_windows_at_least(self):
        self.assert_function_returns(
            count_windows_at_least,
            ([2, 1, 5, 1, 3, 2], 3, 8),
            2,
        )
        self.assert_function_returns(count_windows_at_least, ([1, 1, 1], 2, 5), 0)
        self.assert_function_returns(count_windows_at_least, ([1], 0, 0), 0)
        self.assert_function_returns(count_windows_at_least, ([1, 2], 2, 3), 1)

    def test_max_vowels_in_window(self):
        self.assert_function_returns(max_vowels_in_window, ("abciiidef", 3), 3)
        self.assert_function_returns(max_vowels_in_window, ("rhythm", 2), 0)
        self.assert_function_returns(max_vowels_in_window, ("AEio", 2), 2)
        self.assert_function_returns(max_vowels_in_window, ("AE", 2), 2)

    def test_has_nearby_duplicate(self):
        self.assert_function_returns(has_nearby_duplicate, ([1, 2, 3, 1], 3), True)
        self.assert_function_returns(has_nearby_duplicate, ([1, 2, 3, 1], 2), False)
        self.assert_function_returns(has_nearby_duplicate, ([1, 1], 0), False)

    def test_smallest_subarray_at_least(self):
        self.assert_function_returns(
            smallest_subarray_at_least,
            ([2, 3, 1, 2, 4, 3], 7),
            2,
        )
        self.assert_function_returns(smallest_subarray_at_least, ([1, 1, 1], 5), 0)
        self.assert_function_returns(smallest_subarray_at_least, ([8], 7), 1)

    def test_longest_subarray_at_most(self):
        self.assert_function_returns(longest_subarray_at_most, ([2, 1, 4, 1, 1], 7), 4)
        self.assert_function_returns(longest_subarray_at_most, ([0, 0, 0], 0), 3)
        self.assert_function_returns(longest_subarray_at_most, ([5], 2), 0)

    def test_longest_unique_substring(self):
        self.assert_function_returns(longest_unique_substring, ("abcabcbb",), 3)
        self.assert_function_returns(longest_unique_substring, ("bbbbb",), 1)
        self.assert_function_returns(longest_unique_substring, ("",), 0)

    def test_find_anagram_indices(self):
        self.assert_function_returns(find_anagram_indices, ("cbaebabacd", "abc"), [0, 6])
        self.assert_function_returns(find_anagram_indices, ("abab", "ab"), [0, 1, 2])
        self.assert_function_returns(find_anagram_indices, ("abc", ""), [])
        self.assert_function_returns(find_anagram_indices, ("aaab", "aab"), [1])

    def test_longest_repeating_after_replacements(self):
        self.assert_function_returns(longest_repeating_after_replacements, ("AABABBA", 1), 4)
        self.assert_function_returns(longest_repeating_after_replacements, ("ABAB", 2), 4)
        self.assert_function_returns(longest_repeating_after_replacements, ("", 3), 0)
        self.assert_function_returns(longest_repeating_after_replacements, ("ABC", 1), 2)
        self.assert_function_returns(longest_repeating_after_replacements, ("AAAA", 0), 4)
        self.assert_function_returns(longest_repeating_after_replacements, ("ABC", 5), 3)


if __name__ == "__main__":
    unittest.main()
