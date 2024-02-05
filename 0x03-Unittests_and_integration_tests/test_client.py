#!/usr/bin/env python3
'''0x03. Unittests and Integration Tests'''

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", return_value={"fake": "data"})
    def test_org(self, org_name, mock_get_json):
        # Instantiate GithubOrgClient with the current org_name
        github_client = GithubOrgClient(org_name)

        # Call the org method
        result = github_client.org()

        # Assert that get_json was called once with the expected argument
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/{}".format(org_name))

        self.assertEqual(result, {"fake": "data"})
