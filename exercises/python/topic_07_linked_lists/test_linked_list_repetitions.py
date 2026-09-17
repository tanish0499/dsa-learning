import unittest

from . import linked_lists as exercises


class TestLinkedListRepetitions(unittest.TestCase):
    def call(self, name, *args):
        try:
            return getattr(exercises, name)(*args)
        except NotImplementedError:
            self.skipTest(f"{name} is not implemented yet")

    def nodes(self, head):
        result = []
        seen = set()
        while head is not None:
            self.assertNotIn(id(head), seen, "Result contains a cycle")
            seen.add(id(head))
            result.append(head)
            head = head.next
        return result

    def check_read(self, name, cases):
        for values, extra, expected in cases:
            with self.subTest(values=values, extra=extra):
                head = exercises.build_linked_list(values)
                before = self.nodes(head)
                self.assertEqual(self.call(name, head, *extra), expected)
                self.assertEqual(self.nodes(head), before)
                self.assertEqual([node.value for node in before], values)

    def test_sum_node_values(self):
        self.check_read("sum_node_values", [
            ([4, -2, 7], (), 9), ([], (), 0), ([-3], (), -3),
        ])

    def test_count_occurrences(self):
        self.check_read("count_occurrences", [
            ([4, 7, 4], (4,), 2), ([1, 2], (3,), 0),
            ([], (4,), 0), ([5, 5, 5], (5,), 3),
        ])

    def test_last_value(self):
        self.check_read("last_value", [
            ([4, 7, 2], (), 2), ([0], (), 0), ([], (), None),
        ])

    def test_maximum_value(self):
        self.check_read("maximum_value", [
            ([-4, -7, -2], (), -2), ([9, 1, 9], (), 9),
            ([0], (), 0), ([], (), None),
        ])

    def test_prepend_value(self):
        for values in ([], [7], [4, 7]):
            head = exercises.build_linked_list(values)
            before = self.nodes(head)
            result = self.nodes(self.call("prepend_value", head, 2))
            self.assertEqual([node.value for node in result], [2] + values)
            self.assertEqual(result[1:], before)
            self.assertNotIn(result[0], before)

    def test_insert_after_first(self):
        for values, target in (([], 4), ([4], 4), ([4, 7, 4], 4),
                               ([1, 4], 4), ([1, 2], 9)):
            with self.subTest(values=values, target=target):
                head = exercises.build_linked_list(values)
                before = self.nodes(head)
                result = self.nodes(self.call("insert_after_first", head, target, 8))
                expected = values.copy()
                if target in values:
                    index = values.index(target) + 1
                    expected.insert(index, 8)
                    self.assertEqual(result[:index] + result[index + 1:], before)
                    self.assertNotIn(result[index], before)
                else:
                    self.assertEqual(result, before)
                self.assertEqual([node.value for node in result], expected)

    def test_delete_head(self):
        for values in ([], [4], [4, 7, 2]):
            head = exercises.build_linked_list(values)
            before = self.nodes(head)
            result = self.nodes(self.call("delete_head", head))
            self.assertEqual(result, before[1:])
            self.assertEqual([node.value for node in result], values[1:])

    def test_delete_tail(self):
        for values in ([], [4], [4, 7], [4, 7, 2]):
            head = exercises.build_linked_list(values)
            before = self.nodes(head)
            result = self.nodes(self.call("delete_tail", head))
            self.assertEqual(result, before[:-1])
            self.assertEqual([node.value for node in result], values[:-1])


if __name__ == "__main__":
    unittest.main()
