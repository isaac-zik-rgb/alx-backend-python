#!/usr/bin/env python3
"""A github org client
"""
import unittest
from unittest.mock import patch, Mock
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)
import client
import requests
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """This classs test the GithubOrgClient.org"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self):
        """test_public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "twitter"}
            test_class = GithubOrgClient("twitter")
            self.assertEqual(test_class._public_repos_url, "twitter")
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test_public_repos"""
        mock_get_json.return_value = [{"name": "twitter"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "twitter"
            test_class = GithubOrgClient("twitter")
            self.assertEqual(test_class.public_repos(), ["twitter"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, "my_license", True),
        ({'license': {'key': 'other_license'}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """test_has_license"""
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


@parameterized_class([
    {"org_payload": {"payload": True}, "repos_payload": {"repos_payload": True},
     "expected_repos": ["twitter", "auth-api", "scaffold"]},
    {"org_payload": {"payload": True}, "repos_payload": {"repos_payload": False},
     "expected_repos": []},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """setUpClass"""
        org = "twitter"
        cls.get_patcher = patch('requests.get')
        cls.mock_requests = cls.get_patcher.start()
        cls.mock_requests.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """tearDownClass"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test_public_repos"""
        test_class = GithubOrgClient("twitter")
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("test"), [])
        self.mock_requests.assert_called()

    def test_public_repos_with_license(self):
        """test_public_repos_with_license"""
        test_class = GithubOrgClient("twitter")
        self.assertEqual(test_class.public_repos("apache-2.0"), [])
        self.assertEqual(test_class.public_repos("bsd"), self.expected_repos[0:1])
        self.mock_requests.assert_called()




if __name__ == '__main__':
    unittest.main()
