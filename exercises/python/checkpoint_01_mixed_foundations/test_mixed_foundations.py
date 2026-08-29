import os
import unittest

if os.getenv("DSA_TEST_TARGET") == "solutions":
    from solutions.python.checkpoint_01_mixed_foundations.mixed_foundations_solutions import (
        closest_pair_sum_sorted,
        common_unique_values,
        count_distinct_windows,
        first_nearby_repeat,
        is_subsequence,
        longest_consecutive_run,
        longest_subarray_at_most_k_distinct,
        maximum_sum_distinct_window,
        pair_with_difference_sorted,
        shortest_window_containing_required,
    )
else:
    from .mixed_foundations import (
    closest_pair_sum_sorted,
    common_unique_values,
    count_distinct_windows,
    first_nearby_repeat,
    is_subsequence,
    longest_consecutive_run,
    longest_subarray_at_most_k_distinct,
    maximum_sum_distinct_window,
    pair_with_difference_sorted,
    shortest_window_containing_required,
    )


class TestMixedFoundations(unittest.TestCase):
    def assert_function_returns(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")

        self.assertEqual(actual, expected)

    def test_common_unique_values(self):
        self.assert_function_returns(
            common_unique_values,
            ([4, 2, 4, 1, 3], [3, 4, 4]),
            [4, 3],
        )
        self.assert_function_returns(common_unique_values, ([1, 1], [1]), [1])
        self.assert_function_returns(common_unique_values, ([], [1]), [])

    def test_is_subsequence(self):
        self.assert_function_returns(is_subsequence, ("ace", "abcde"), True)
        self.assert_function_returns(is_subsequence, ("aec", "abcde"), False)
        self.assert_function_returns(is_subsequence, ("", "abc"), True)
        self.assert_function_returns(is_subsequence, ("abc", ""), False)

    def test_first_nearby_repeat(self):
        self.assert_function_returns(first_nearby_repeat, ([5, 1, 2, 1, 5], 2), 1)
        self.assert_function_returns(first_nearby_repeat, ([5, 1, 2, 1, 5], 3), 1)
        self.assert_function_returns(first_nearby_repeat, ([1, 2, 1], 1), None)
        self.assert_function_returns(first_nearby_repeat, ([1, 1], 0), None)

    def test_pair_with_difference_sorted(self):
        self.assert_function_returns(pair_with_difference_sorted, ([1, 3, 5, 8], 3), True)
        self.assert_function_returns(pair_with_difference_sorted, ([1, 3, 5, 8], 4), True)
        self.assert_function_returns(pair_with_difference_sorted, ([1, 3, 5, 8], 6), False)
        self.assert_function_returns(pair_with_difference_sorted, ([2, 2], 0), True)
        self.assert_function_returns(pair_with_difference_sorted, ([2], 0), False)

    def test_count_distinct_windows(self):
        self.assert_function_returns(count_distinct_windows, ("abac", 3), 1)
        self.assert_function_returns(count_distinct_windows, ("abcd", 2), 3)
        self.assert_function_returns(count_distinct_windows, ("aaaa", 1), 4)
        self.assert_function_returns(count_distinct_windows, ("abc", 0), 0)

    def test_maximum_sum_distinct_window(self):
        self.assert_function_returns(
            maximum_sum_distinct_window,
            ([1, 5, 4, 2, 9, 9, 9], 3),
            15,
        )
        self.assert_function_returns(maximum_sum_distinct_window, ([-5, -2, -3], 2), -5)
        self.assert_function_returns(maximum_sum_distinct_window, ([1, 1, 1], 2), None)
        self.assert_function_returns(maximum_sum_distinct_window, ([1], 2), None)

    def test_longest_subarray_at_most_k_distinct(self):
        self.assert_function_returns(
            longest_subarray_at_most_k_distinct,
            ([1, 2, 1, 2, 3], 2),
            4,
        )
        self.assert_function_returns(
            longest_subarray_at_most_k_distinct,
            ([1, 2, 1, 3, 4], 3),
            4,
        )
        self.assert_function_returns(longest_subarray_at_most_k_distinct, ([], 2), 0)
        self.assert_function_returns(longest_subarray_at_most_k_distinct, ([1], 0), 0)

    def test_shortest_window_containing_required(self):
        self.assert_function_returns(
            shortest_window_containing_required,
            ([1, 2, 2, 3, 1, 2], [1, 3]),
            2,
        )
        self.assert_function_returns(
            shortest_window_containing_required,
            ([1, 2, 3], [1, 2, 3]),
            3,
        )
        self.assert_function_returns(shortest_window_containing_required, ([1, 2], [3]), 0)
        self.assert_function_returns(shortest_window_containing_required, ([1, 2], []), 0)

    def test_closest_pair_sum_sorted(self):
        self.assert_function_returns(closest_pair_sum_sorted, ([1, 3, 4, 7, 10], 15), 14)
        self.assert_function_returns(closest_pair_sum_sorted, ([1, 4, 6], 6), 5)
        self.assert_function_returns(closest_pair_sum_sorted, ([-5, -2, 3, 9], 0), 1)
        self.assert_function_returns(closest_pair_sum_sorted, ([1], 5), None)

    def test_longest_consecutive_run(self):
        self.assert_function_returns(longest_consecutive_run, ([100, 4, 200, 1, 3, 2],), 4)
        self.assert_function_returns(longest_consecutive_run, ([1, 2, 2, 3],), 3)
        self.assert_function_returns(longest_consecutive_run, ([-1, 1, 0, 2],), 4)
        self.assert_function_returns(longest_consecutive_run, ([],), 0)


if __name__ == "__main__":
    unittest.main()
