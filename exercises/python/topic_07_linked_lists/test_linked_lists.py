import unittest

from .linked_lists import (
    append_value,
    build_linked_list,
    contains_value,
    delete_first_value,
    has_cycle,
    linked_list_length,
    linked_list_to_list,
    merge_sorted_lists,
    middle_value,
    remove_nth_from_end,
    reverse_linked_list,
    value_at_index,
)


class TestLinkedLists(unittest.TestCase):
    def assert_function_returns(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")

        self.assertEqual(actual, expected)

    def assert_linked_values(self, function, args, expected):
        try:
            head = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")

        self.assertEqual(linked_list_to_list(head), expected)

    def test_linked_list_length(self):
        self.assert_function_returns(linked_list_length, (build_linked_list([4, 7, 2]),), 3)
        self.assert_function_returns(linked_list_length, (build_linked_list([1]),), 1)
        self.assert_function_returns(linked_list_length, (None,), 0)

    def test_contains_value(self):
        head = build_linked_list([4, 7, 2])
        self.assert_function_returns(contains_value, (head, 7), True)
        self.assert_function_returns(contains_value, (head, 6), False)
        self.assert_function_returns(contains_value, (None, 1), False)

    def test_value_at_index(self):
        head = build_linked_list([4, 7, 2])
        self.assert_function_returns(value_at_index, (head, 0), 4)
        self.assert_function_returns(value_at_index, (head, 2), 2)
        self.assert_function_returns(value_at_index, (head, 3), None)
        self.assert_function_returns(value_at_index, (head, -1), None)

    def test_append_value(self):
        self.assert_linked_values(append_value, (build_linked_list([4, 7]), 2), [4, 7, 2])
        self.assert_linked_values(append_value, (None, 5), [5])

    def test_delete_first_value(self):
        self.assert_linked_values(delete_first_value, (build_linked_list([1, 2, 1]), 1), [2, 1])
        self.assert_linked_values(delete_first_value, (build_linked_list([1, 2]), 3), [1, 2])
        self.assert_linked_values(delete_first_value, (None, 1), [])

    def test_reverse_linked_list(self):
        self.assert_linked_values(reverse_linked_list, (build_linked_list([1, 2, 3]),), [3, 2, 1])
        self.assert_linked_values(reverse_linked_list, (build_linked_list([1]),), [1])
        self.assert_linked_values(reverse_linked_list, (None,), [])

    def test_middle_value(self):
        self.assert_function_returns(middle_value, (build_linked_list([1, 2, 3]),), 2)
        self.assert_function_returns(middle_value, (build_linked_list([1, 2, 3, 4]),), 3)
        self.assert_function_returns(middle_value, (None,), None)

    def test_merge_sorted_lists(self):
        self.assert_linked_values(
            merge_sorted_lists,
            (build_linked_list([1, 3, 5]), build_linked_list([2, 4])),
            [1, 2, 3, 4, 5],
        )
        self.assert_linked_values(merge_sorted_lists, (None, build_linked_list([1, 2])), [1, 2])

    def test_remove_nth_from_end(self):
        self.assert_linked_values(
            remove_nth_from_end,
            (build_linked_list([1, 2, 3, 4, 5]), 2),
            [1, 2, 3, 5],
        )
        self.assert_linked_values(remove_nth_from_end, (build_linked_list([1, 2]), 2), [2])
        self.assert_linked_values(remove_nth_from_end, (build_linked_list([1, 2]), 3), [1, 2])
        self.assert_linked_values(remove_nth_from_end, (build_linked_list([1, 2]), 0), [1, 2])

    def test_has_cycle(self):
        acyclic = build_linked_list([1, 2, 3])
        self.assert_function_returns(has_cycle, (acyclic,), False)

        cyclic = build_linked_list([1, 2, 3, 4])
        cyclic.next.next.next.next = cyclic.next
        self.assert_function_returns(has_cycle, (cyclic,), True)
        self.assert_function_returns(has_cycle, (None,), False)


if __name__ == "__main__":
    unittest.main()
