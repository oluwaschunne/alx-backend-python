#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests"""

from typing import Dict, Mapping, Sequence, Union
from unittest import TestCase

from parameterized import parameterized
from utils import access_nested_map


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
