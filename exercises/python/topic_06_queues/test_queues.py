import unittest

from .queues import (
    first_non_repeating_stream,
    generate_binary_numbers,
    last_n_events,
    moving_averages,
    process_queue_operations,
    reverse_first_k,
    round_robin_completion_order,
    serve_customers,
    sliding_window_maximum,
    time_to_buy_tickets,
)


class TestQueues(unittest.TestCase):
    def assert_function_returns(self, function, args, expected):
        try:
            actual = function(*args)
        except NotImplementedError:
            self.skipTest(f"{function.__name__} is not implemented yet")

        self.assertEqual(actual, expected)

    def test_process_queue_operations(self):
        operations = [
            ("enqueue", 10),
            ("enqueue", 20),
            ("dequeue", None),
            ("peek", None),
            ("dequeue", None),
        ]
        self.assert_function_returns(process_queue_operations, (operations,), [10, 20, 20])
        self.assert_function_returns(
            process_queue_operations,
            ([('dequeue', None), ('peek', None)],),
            [None, None],
        )

    def test_serve_customers(self):
        self.assert_function_returns(
            serve_customers,
            (["A", "B", "C"], 2),
            (["A", "B"], ["C"]),
        )
        self.assert_function_returns(serve_customers, (["A"], 3), (["A"], []))
        self.assert_function_returns(serve_customers, (["A"], 0), ([], ["A"]))

    def test_last_n_events(self):
        self.assert_function_returns(last_n_events, (["a", "b", "c", "d"], 2), ["c", "d"])
        self.assert_function_returns(last_n_events, ([1, 2], 5), [1, 2])
        self.assert_function_returns(last_n_events, ([1, 2], 0), [])

    def test_reverse_first_k(self):
        self.assert_function_returns(reverse_first_k, ([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5])
        self.assert_function_returns(reverse_first_k, ([1, 2], 3), [1, 2])
        self.assert_function_returns(reverse_first_k, ([], 0), [])

    def test_moving_averages(self):
        self.assert_function_returns(moving_averages, ([1, 2, 3, 4], 3), [2.0, 3.0])
        self.assert_function_returns(moving_averages, ([-2, 2], 2), [0.0])
        self.assert_function_returns(moving_averages, ([1], 2), [])

    def test_first_non_repeating_stream(self):
        self.assert_function_returns(first_non_repeating_stream, ("aabc",), ["a", None, "b", "b"])
        self.assert_function_returns(first_non_repeating_stream, ("abc",), ["a", "a", "a"])
        self.assert_function_returns(first_non_repeating_stream, ("",), [])

    def test_time_to_buy_tickets(self):
        self.assert_function_returns(time_to_buy_tickets, ([2, 3, 2], 2), 6)
        self.assert_function_returns(time_to_buy_tickets, ([5, 1, 1, 1], 0), 8)
        self.assert_function_returns(time_to_buy_tickets, ([1], 0), 1)

    def test_round_robin_completion_order(self):
        self.assert_function_returns(
            round_robin_completion_order,
            ([('A', 3), ('B', 1), ('C', 2)], 2),
            ["B", "C", "A"],
        )
        self.assert_function_returns(round_robin_completion_order, ([], 2), [])

    def test_generate_binary_numbers(self):
        self.assert_function_returns(generate_binary_numbers, (5,), ["1", "10", "11", "100", "101"])
        self.assert_function_returns(generate_binary_numbers, (1,), ["1"])
        self.assert_function_returns(generate_binary_numbers, (0,), [])

    def test_sliding_window_maximum(self):
        self.assert_function_returns(
            sliding_window_maximum,
            ([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7],
        )
        self.assert_function_returns(sliding_window_maximum, ([4, 2], 1), [4, 2])
        self.assert_function_returns(sliding_window_maximum, ([1], 2), [])


if __name__ == "__main__":
    unittest.main()
