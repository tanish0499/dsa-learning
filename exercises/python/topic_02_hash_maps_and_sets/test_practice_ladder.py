import unittest

from .practice_ladder import (
    common_values_once,
    contains_all_values,
    count_words,
    group_words_by_length,
    same_frequencies,
    values_appearing_once,
)


class TestHashMapsSetsPracticeLadder(unittest.TestCase):
    def check(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")
        self.assertEqual(actual, expected)

    def test_contains_all_values(self):
        self.check(contains_all_values, ([1, 2, 3], [3, 1]), True)
        self.check(contains_all_values, ([1, 2], [1, 3]), False)
        self.check(contains_all_values, ([1], []), True)

    def test_common_values_once(self):
        self.check(common_values_once, ([3, 1, 3, 2], [2, 3]), [3, 2])
        self.check(common_values_once, ([1], [2]), [])

    def test_count_words(self):
        self.check(count_words, (["dev", "ops", "dev"],), {"dev": 2, "ops": 1})
        self.check(count_words, ([],), {})

    def test_values_appearing_once(self):
        self.check(values_appearing_once, ([4, 2, 4, 3],), [2, 3])
        self.check(values_appearing_once, ([1, 1],), [])

    def test_same_frequencies(self):
        self.check(same_frequencies, ([1, 2, 1], [2, 1, 1]), True)
        self.check(same_frequencies, ([1, 2], [1, 1]), False)

    def test_group_words_by_length(self):
        self.check(
            group_words_by_length,
            (["a", "to", "be", "cat"],),
            {1: ["a"], 2: ["to", "be"], 3: ["cat"]},
        )
        self.check(group_words_by_length, ([],), {})


if __name__ == "__main__":
    unittest.main()
