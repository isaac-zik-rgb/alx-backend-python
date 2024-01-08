#!/usr/bin/env python3
"""A github org client
"""
import unittest
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


if __name__ == '__main__':
    unittest.main()
