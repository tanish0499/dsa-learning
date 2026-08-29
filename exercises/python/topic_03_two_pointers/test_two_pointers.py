import os
import unittest

if os.getenv("DSA_TEST_TARGET") == "solutions":
    from solutions.python.topic_03_two_pointers.two_pointers_solutions import (
        has_three_sum_sorted,
        is_palindrome,
        max_water_container,
        merge_sorted_lists,
        move_zeros_to_end,
        pair_sum_sorted,
        remove_duplicates_sorted,
        reverse_values,
        sorted_squares,
        valid_palindrome,
    )
else:
    from .two_pointers import (
    has_three_sum_sorted,
    is_palindrome,
    max_water_container,
    merge_sorted_lists,
    move_zeros_to_end,
    pair_sum_sorted,
    remove_duplicates_sorted,
    reverse_values,
    sorted_squares,
    valid_palindrome,
    )


class TestTwoPointers(unittest.TestCase):
    def assert_function_returns(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")

        self.assertEqual(actual, expected)

    def test_reverse_values(self):
        self.assert_function_returns(reverse_values, ([1, 2, 3, 4],), [4, 3, 2, 1])
        self.assert_function_returns(reverse_values, ([1, 2, 3],), [3, 2, 1])
        self.assert_function_returns(reverse_values, ([5],), [5])
        self.assert_function_returns(reverse_values, ([],), [])

    def test_is_palindrome(self):
        self.assert_function_returns(is_palindrome, ("level",), True)
        self.assert_function_returns(is_palindrome, ("python",), False)
        self.assert_function_returns(is_palindrome, ("",), True)

    def test_pair_sum_sorted(self):
        self.assert_function_returns(pair_sum_sorted, ([1, 2, 4, 7, 9], 11), True)
        self.assert_function_returns(pair_sum_sorted, ([1, 2, 4, 7, 9], 20), False)
        self.assert_function_returns(pair_sum_sorted, ([5], 10), False)
        self.assert_function_returns(pair_sum_sorted, ([5, 5], 10), True)

    def test_merge_sorted_lists(self):
        self.assert_function_returns(
            merge_sorted_lists,
            ([1, 4, 7], [2, 3, 8]),
            [1, 2, 3, 4, 7, 8],
        )
        self.assert_function_returns(merge_sorted_lists, ([], [1, 2]), [1, 2])
        self.assert_function_returns(merge_sorted_lists, ([1, 1], [1]), [1, 1, 1])

    def test_remove_duplicates_sorted(self):
        self.assert_function_returns(
            remove_duplicates_sorted,
            ([1, 1, 2, 2, 2, 3],),
            [1, 2, 3],
        )
        self.assert_function_returns(remove_duplicates_sorted, ([],), [])
        self.assert_function_returns(remove_duplicates_sorted, ([4, 4, 4],), [4])

    def test_move_zeros_to_end(self):
        self.assert_function_returns(
            move_zeros_to_end,
            ([0, 1, 0, 3, 12],),
            [1, 3, 12, 0, 0],
        )
        self.assert_function_returns(move_zeros_to_end, ([1, 2],), [1, 2])
        self.assert_function_returns(move_zeros_to_end, ([0, 0],), [0, 0])

    def test_sorted_squares(self):
        self.assert_function_returns(
            sorted_squares,
            ([-4, -1, 0, 3, 10],),
            [0, 1, 9, 16, 100],
        )
        self.assert_function_returns(sorted_squares, ([-3, -2, -1],), [1, 4, 9])
        self.assert_function_returns(sorted_squares, ([],), [])

    def test_valid_palindrome(self):
        self.assert_function_returns(
            valid_palindrome,
            ("A man, a plan, a canal: Panama",),
            True,
        )
        self.assert_function_returns(valid_palindrome, ("race a car",), False)
        self.assert_function_returns(valid_palindrome, (".,",), True)

    def test_has_three_sum_sorted(self):
        self.assert_function_returns(has_three_sum_sorted, ([1, 2, 3, 4, 7], 10), True)
        self.assert_function_returns(has_three_sum_sorted, ([1, 2, 3, 4, 5], 9), True)
        self.assert_function_returns(has_three_sum_sorted, ([1, 2, 4, 8], 20), False)
        self.assert_function_returns(has_three_sum_sorted, ([2, 2, 2], 6), True)

    def test_max_water_container(self):
        self.assert_function_returns(
            max_water_container,
            ([1, 8, 6, 2, 5, 4, 8, 3, 7],),
            49,
        )
        self.assert_function_returns(max_water_container, ([1, 1],), 1)
        self.assert_function_returns(max_water_container, ([10, 1, 1, 10, 1],), 30)
        self.assert_function_returns(max_water_container, ([],), 0)


if __name__ == "__main__":
    unittest.main()
