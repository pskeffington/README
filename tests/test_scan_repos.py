import unittest
from unittest.mock import patch

from scripts.scan_repos import collect_repos


class CollectReposTests(unittest.TestCase):
    @patch("scripts.scan_repos.request_json")
    def test_default_token_uses_public_owner_endpoint(self, request_json):
        request_json.side_effect = [
            [{"name": "README", "owner": {"login": "pskeffington"}}],
            [],
        ]

        repos = collect_repos("pskeffington", "actions-token")

        self.assertEqual([repo["name"] for repo in repos], ["README"])
        first_url = request_json.call_args_list[0].args[0]
        self.assertIn("/users/pskeffington/repos", first_url)
        self.assertNotIn("/user/repos", first_url)

    @patch("scripts.scan_repos.request_json")
    def test_explicit_private_token_uses_authenticated_endpoint(self, request_json):
        request_json.side_effect = [
            [{"name": "trans", "owner": {"login": "pskeffington"}}],
            [],
        ]

        repos = collect_repos("pskeffington", "private-token", include_private=True)

        self.assertEqual([repo["name"] for repo in repos], ["trans"])
        first_url = request_json.call_args_list[0].args[0]
        self.assertIn("/user/repos", first_url)
        self.assertIn("affiliation=owner,collaborator,organization_member", first_url)

    @patch("scripts.scan_repos.request_json")
    def test_foreign_owned_repositories_are_filtered(self, request_json):
        request_json.side_effect = [
            [
                {"name": "owned", "owner": {"login": "pskeffington"}},
                {"name": "foreign", "owner": {"login": "someone-else"}},
            ],
            [],
        ]

        repos = collect_repos("pskeffington", None)

        self.assertEqual([repo["name"] for repo in repos], ["owned"])


if __name__ == "__main__":
    unittest.main()
