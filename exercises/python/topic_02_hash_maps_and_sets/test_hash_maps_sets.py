import os
import unittest

if os.getenv("DSA_TEST_TARGET") == "solutions":
    from solutions.python.topic_02_hash_maps_and_sets.hash_maps_sets_solutions import (
        count_characters,
        count_values,
        first_non_repeating_character,
        first_repeated_value,
        group_words_by_first_letter,
        has_duplicate,
        is_anagram,
        most_frequent_value,
        two_sum,
        unique_values,
    )
else:
    from .hash_maps_sets import (
    count_characters,
    count_values,
    first_non_repeating_character,
    first_repeated_value,
    group_words_by_first_letter,
    has_duplicate,
    is_anagram,
    most_frequent_value,
    two_sum,
    unique_values,
    )


class TestHashMapsAndSets(unittest.TestCase):
    def assert_function_returns(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")

        self.assertEqual(actual, expected)

    def test_has_duplicate(self):
        self.assert_function_returns(has_duplicate, ([2, 5, 2, 9],), True)
        self.assert_function_returns(has_duplicate, ([1, 2, 3],), False)
        self.assert_function_returns(has_duplicate, ([],), False)

    def test_count_values(self):
        self.assert_function_returns(
            count_values,
            (["dev", "ops", "dev"],),
            {"dev": 2, "ops": 1},
        )
        self.assert_function_returns(count_values, ([],), {})
        self.assert_function_returns(count_values, ([1, 1, 2, 3, 2],), {1: 2, 2: 2, 3: 1})

    def test_count_characters(self):
        self.assert_function_returns(
            count_characters,
            ("hello",),
            {"h": 1, "e": 1, "l": 2, "o": 1},
        )
        self.assert_function_returns(count_characters, ("",), {})

    def test_first_repeated_value(self):
        self.assert_function_returns(first_repeated_value, ([5, 1, 3, 1, 5],), 1)
        self.assert_function_returns(first_repeated_value, ([4, 4, 2, 2],), 4)
        self.assert_function_returns(first_repeated_value, ([1, 2, 3],), None)

    def test_unique_values(self):
        self.assert_function_returns(
            unique_values,
            (["a", "b", "a", "c", "b"],),
            ["a", "b", "c"],
        )
        self.assert_function_returns(unique_values, ([],), [])
        self.assert_function_returns(unique_values, ([3, 3, 1, 3, 2],), [3, 1, 2])

    def test_most_frequent_value(self):
        self.assert_function_returns(most_frequent_value, (["a", "b", "a", "c"],), "a")
        self.assert_function_returns(most_frequent_value, ([5, 1, 5, 1, 1],), 1)
        self.assert_function_returns(most_frequent_value, (["x"],), "x")

    def test_two_sum(self):
        self.assert_function_returns(two_sum, ([4, 2, 7, 1], 9), True)
        self.assert_function_returns(two_sum, ([4, 2, 7, 1], 8), True)
        self.assert_function_returns(two_sum, ([4, 2, 7, 1], 20), False)
        self.assert_function_returns(two_sum, ([5], 10), False)

    def test_is_anagram(self):
        self.assert_function_returns(is_anagram, ("listen", "silent"), True)
        self.assert_function_returns(is_anagram, ("apple", "papel"), True)
        self.assert_function_returns(is_anagram, ("rat", "car"), False)
        self.assert_function_returns(is_anagram, ("aabb", "ab"), False)

    def test_group_words_by_first_letter(self):
        self.assert_function_returns(
            group_words_by_first_letter,
            (["dev", "dog", "ops"],),
            {"d": ["dev", "dog"], "o": ["ops"]},
        )
        self.assert_function_returns(group_words_by_first_letter, ([],), {})

    def test_first_non_repeating_character(self):
        self.assert_function_returns(first_non_repeating_character, ("swiss",), "w")
        self.assert_function_returns(first_non_repeating_character, ("aabbcc",), None)
        self.assert_function_returns(first_non_repeating_character, ("",), None)


if __name__ == "__main__":
    unittest.main()
