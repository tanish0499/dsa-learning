import unittest

from .stacks import (
    apply_backspaces,
    daily_warmer_waits,
    evaluate_postfix,
    is_balanced_parentheses,
    next_greater_values,
    remove_adjacent_duplicates,
    reverse_with_stack,
    simplify_unix_path,
    stock_spans,
    validate_stack_sequences,
)


class TestStacks(unittest.TestCase):
    def assert_function_returns(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")

        self.assertEqual(actual, expected)

    def test_reverse_with_stack(self):
        self.assert_function_returns(reverse_with_stack, ([4, 7, 2],), [2, 7, 4])
        self.assert_function_returns(reverse_with_stack, ([],), [])
        self.assert_function_returns(reverse_with_stack, ([1],), [1])

    def test_apply_backspaces(self):
        self.assert_function_returns(apply_backspaces, ("ab#c",), "ac")
        self.assert_function_returns(apply_backspaces, ("a##b",), "b")
        self.assert_function_returns(apply_backspaces, ("###",), "")
        self.assert_function_returns(apply_backspaces, ("abc",), "abc")

    def test_is_balanced_parentheses(self):
        self.assert_function_returns(is_balanced_parentheses, ("a + ([b])",), True)
        self.assert_function_returns(is_balanced_parentheses, ("([)]",), False)
        self.assert_function_returns(is_balanced_parentheses, ("{[]}",), True)
        self.assert_function_returns(is_balanced_parentheses, ("]",), False)

    def test_remove_adjacent_duplicates(self):
        self.assert_function_returns(remove_adjacent_duplicates, ("abbaca",), "ca")
        self.assert_function_returns(remove_adjacent_duplicates, ("azxxzy",), "ay")
        self.assert_function_returns(remove_adjacent_duplicates, ("",), "")

    def test_evaluate_postfix(self):
        self.assert_function_returns(evaluate_postfix, (["2", "1", "+", "3", "*"],), 9)
        self.assert_function_returns(evaluate_postfix, (["4", "13", "5", "/", "+"],), 6)
        self.assert_function_returns(evaluate_postfix, (["-7", "3", "/"],), -2)

    def test_simplify_unix_path(self):
        self.assert_function_returns(simplify_unix_path, ("/home//ops/../logs/",), "/home/logs")
        self.assert_function_returns(simplify_unix_path, ("/../",), "/")
        self.assert_function_returns(simplify_unix_path, ("/a/./b/../../c/",), "/c")

    def test_validate_stack_sequences(self):
        self.assert_function_returns(validate_stack_sequences, ([1, 2, 3], [2, 3, 1]), True)
        self.assert_function_returns(validate_stack_sequences, ([1, 2, 3], [3, 1, 2]), False)
        self.assert_function_returns(validate_stack_sequences, ([], []), True)

    def test_next_greater_values(self):
        self.assert_function_returns(next_greater_values, ([2, 1, 5, 3],), [5, 5, -1, -1])
        self.assert_function_returns(next_greater_values, ([3, 2, 1],), [-1, -1, -1])
        self.assert_function_returns(next_greater_values, ([2, 2, 3],), [3, 3, -1])

    def test_daily_warmer_waits(self):
        self.assert_function_returns(daily_warmer_waits, ([73, 74, 71, 75],), [1, 2, 1, 0])
        self.assert_function_returns(daily_warmer_waits, ([80, 79],), [0, 0])
        self.assert_function_returns(daily_warmer_waits, ([],), [])

    def test_stock_spans(self):
        self.assert_function_returns(
            stock_spans,
            ([100, 80, 60, 70, 60, 75, 85],),
            [1, 1, 1, 2, 1, 4, 6],
        )
        self.assert_function_returns(stock_spans, ([10, 20, 30],), [1, 2, 3])
        self.assert_function_returns(stock_spans, ([30, 20, 10],), [1, 1, 1])


if __name__ == "__main__":
    unittest.main()
