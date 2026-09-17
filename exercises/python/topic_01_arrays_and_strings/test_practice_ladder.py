import unittest

from .practice_ladder import (
    count_greater_than,
    find_minimum,
    first_index_of,
    longest_word,
    running_sums,
    sum_positive_numbers,
)


class TestArraysStringsPracticeLadder(unittest.TestCase):
    def check(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")
        self.assertEqual(actual, expected)

    def test_count_greater_than(self):
        self.check(count_greater_than, ([2, 8, 5, 10], 5), 2)
        self.check(count_greater_than, ([], 3), 0)

    def test_sum_positive_numbers(self):
        self.check(sum_positive_numbers, ([-2, 0, 4, 3],), 7)
        self.check(sum_positive_numbers, ([-2, -1],), 0)

    def test_find_minimum(self):
        self.check(find_minimum, ([5, -1, 3],), -1)
        self.check(find_minimum, ([],), None)

    def test_first_index_of(self):
        self.check(first_index_of, ([4, 2, 4], 4), 0)
        self.check(first_index_of, ([1, 2], 3), -1)

    def test_running_sums(self):
        self.check(running_sums, ([2, 3, 5],), [2, 5, 10])
        self.check(running_sums, ([],), [])

    def test_longest_word(self):
        self.check(longest_word, (["dev", "cloud", "tools"],), "cloud")
        self.check(longest_word, ([],), None)


if __name__ == "__main__":
    unittest.main()
