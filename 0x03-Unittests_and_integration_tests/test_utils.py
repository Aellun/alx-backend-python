#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    Test suite for access_nested_map function from utils module.

    This class contains unit tests that verify the functionality of
    the access_nested_map function using various test cases.
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        Test access_nested_map with various inputs and expected outputs.
            The function is tested with three different sets of inputs
            to ensure that it correctly navigates through the nested map
            and returns the expected value.
        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path of keys to navigate through the nested_map.
            expected: The expected value that should be returned.
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
