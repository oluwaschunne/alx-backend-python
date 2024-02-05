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

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_public_repos_url(self, org_name):
        # Mock the org method to return a known payload
        with patch.object(GithubOrgClient, 'org', return_value={"repos_url": "https://api.github.com/repos"}):
            github_client = GithubOrgClient(org_name)

            result = github_client._public_repos_url

            expected_url = "https://api.github.com/repos"
            self.assertEqual(result, expected_url)

    @parameterized.expand([
        ("google", ["repo1", "repo2"]),
        ("abc", ["repo3", "repo4"]),
    ])
    @patch("client.get_json", return_value={"fake": "data"})
    @patch.object(GithubOrgClient, '_public_repos_url', return_value="https://api.github.com/repos")
    def test_public_repos(self, org_name, expected_repos, mock_public_repos_url, mock_get_json):
        github_client = GithubOrgClient(org_name)

        result = github_client.public_repos()

        mock_get_json.assert_called_once_with("https://api.github.com/repos")

        self.assertEqual(result, expected_repos)
