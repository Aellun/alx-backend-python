#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''''
        Test that access_nested_map raises a KeyError with the correct message
        when the path does not exist in the nested map.
        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path of keys to navigate through the nested_map.
        '''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Verify that the exception message is as expected
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    ''''
        Test suite for the get_json function from utils module.
        This class contains unit tests that verify the functionality of
        the get_json function using mocked HTTP responses.
    '''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''
            Test that get_json returns the expected result
            from the mocked requests.get.
            Args:
                test_url (str): The URL to be passed to get_json.
                test_payload (dict): The expected payload to be returned
                mock_get (Mock): The mocked requests.get method.
        '''
        # Create a Mock response object with a json method
        # that returns test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function with the test_url
        result = get_json(test_url)

        # Assert that requests.get was called
        # exactly once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the result of get_json is
        # equal to the test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''
        Test suite for the memoize decorator from utils module.
        This class contains unit tests that verify the functionality of
        the memoize decorator by testing its caching behavior.
    '''

    def test_memoize(self):
        '''
        Test that the memoize decorator correctly
        caches method results.
        '''

        # Define a class with a memoized property
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Use patch to mock the a_method
        with patch.object(test_instance,
                          'a_method',
                          return_value=42) as mock_a_method:
            # Call the memoized property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Verify that the result is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Verify that a_method was called only once
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
