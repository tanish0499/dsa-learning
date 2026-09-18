import copy
import unittest

from . import recursion


class TestRecursion(unittest.TestCase):
    def check_cases(self, function, cases):
        for args, expected in cases:
            before = copy.deepcopy(args)
            try:
                actual = function(*args)
            except NotImplementedError:
                self.skipTest(f"{function.__name__} is not implemented yet")
            self.assertEqual(actual, expected, f"Input: {before!r}")
            self.assertEqual(args, before, "Do not mutate the input")

    def test_count_down(self):
        self.check_cases(recursion.count_down, [((3,), [3, 2, 1]), ((0,), []), ((1,), [1])])

    def test_count_up(self):
        self.check_cases(recursion.count_up, [((3,), [1, 2, 3]), ((0,), []), ((1,), [1])])

    def test_sum_to_n(self):
        self.check_cases(recursion.sum_to_n, [((4,), 10), ((0,), 0), ((1,), 1)])

    def test_sum_even_to_n(self):
        self.check_cases(recursion.sum_even_to_n, [((5,), 6), ((6,), 12), ((0,), 0), ((1,), 0)])

    def test_factorial(self):
        self.check_cases(recursion.factorial, [((4,), 24), ((0,), 1), ((1,), 1)])

    def test_power(self):
        self.check_cases(recursion.power, [((2, 4), 16), ((-2, 3), -8), ((0, 0), 1), ((0, 3), 0)])

    def test_sum_digits(self):
        self.check_cases(recursion.sum_digits, [((402,), 6), ((0,), 0), ((9,), 9)])

    def test_count_digits(self):
        self.check_cases(recursion.count_digits, [((402,), 3), ((0,), 1), ((9,), 1), ((1000,), 4)])

    def test_sum_values(self):
        self.check_cases(recursion.sum_values, [(([2, -3, 5],), 4), (([],), 0), (([-4],), -4)])

    def test_count_target(self):
        self.check_cases(recursion.count_target, [(([2, 1, 2], 2), 2), (([], 2), 0), (([1, 3], 2), 0)])

    def test_contains_value(self):
        self.check_cases(recursion.contains_value, [(([1, 3, 5], 5), True), (([1, 3], 2), False), (([], 1), False)])

    def test_maximum_value(self):
        self.check_cases(recursion.maximum_value, [(([-5, -2, -9],), -2), (([],), None), (([7],), 7), (([9, 2, 9],), 9)])

    def test_first_index(self):
        self.check_cases(recursion.first_index, [(([4, 2, 4], 4), 0), (([4, 2, 7], 7), 2), (([], 1), -1), (([2], 1), -1)])

    def test_reverse_text(self):
        self.check_cases(recursion.reverse_text, [(('abc',), 'cba'), (('',), ''), (('x',), 'x')])

    def test_count_character(self):
        self.check_cases(recursion.count_character, [(('banana', 'a'), 3), (('', 'a'), 0), (('AaA', 'a'), 1)])

    def test_remove_character(self):
        self.check_cases(recursion.remove_character, [(('banana', 'a'), 'bnn'), (('', 'a'), ''), (('aaa', 'a'), ''), (('abc', 'x'), 'abc')])

    def test_is_palindrome(self):
        self.check_cases(recursion.is_palindrome, [(('abba',), True), (('abcba',), True), (('ab',), False), (('',), True), (('Aa',), False)])

    def test_is_sorted(self):
        self.check_cases(recursion.is_sorted, [(([1, 2, 2, 4],), True), (([1, 3, 2],), False), (([],), True), (([5],), True)])

    def test_fibonacci(self):
        self.check_cases(recursion.fibonacci, [((0,), 0), ((1,), 1), ((6,), 8), ((8,), 21)])

    def test_count_stair_ways(self):
        self.check_cases(recursion.count_stair_ways, [((0,), 1), ((1,), 1), ((2,), 2), ((3,), 3), ((5,), 8)])


if __name__ == "__main__":
    unittest.main()
