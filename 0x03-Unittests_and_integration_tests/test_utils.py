#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests"""

import unittest
from typing import Dict, Mapping, Sequence, Union
from unittest import TestCase
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(TestCase):
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict, path: Sequence, return_val: Union[int, Dict]
    ) -> None:
        """Test access nested map functionality"""
        self.assertEqual(
            access_nested_map(nested_map=nested_map, path=path), return_val
        )

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):

    @patch("utils.requests.get")
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        # Configure the mock_get to return a MagicMock with a json method
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function
        result = get_json(test_url)

        # Assert that the mocked get method was called exactly once with test_url as argument
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):

    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        # Create an instance of TestClass
        test_instance = self.TestClass()

        # Configure the mock_a_method to return 42
        mock_a_method.return_value = 42

        # Call a_property twice
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        # Assert that a_method was called only once
        mock_a_method.assert_called_once()

        # Assert that the results are correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
