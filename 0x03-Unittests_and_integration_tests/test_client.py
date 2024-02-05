#!/usr/bin/env python3
'''0x03. Unittests and Integration Tests'''

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        github_client = GithubOrgClient("example_org")

        # Call the has_license method with the provided input
        result = github_client.has_license(repo, license_key)

        self.assertEqual(result, expected_result)

    @parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (org_payload, repos_payload, expected_repos, apache2_repos),
    ]
    )

class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Mock requests.get using patch
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            MagicMock(json=lambda: cls.org_payload),
            MagicMock(json=lambda: cls.repos_payload),
            # Add more mocks as needed
        ]

    @classmethod
    def tearDownClass(cls):
        # Stop the patcher in tearDownClass
        cls.get_patcher.stop()

    def test_public_repos(self):
        github_client = GithubOrgClient("example_org")
        github_client.org = MagicMock(return_value=self.org_payload)

        # Call the public_repos method
        result = github_client.public_repos()

        # Assert that the result is as expected based on the fixture
        self.assertEqual(result, self.expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        github_client = GithubOrgClient("example_org")

        # Call the has_license method with the provided input
        result = github_client.has_license(repo, license_key)

        # Assert that the result is the expected value
        self.assertEqual(result, expected_result)
