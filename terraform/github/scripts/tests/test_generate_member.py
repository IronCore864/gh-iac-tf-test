import unittest
from unittest.mock import MagicMock, patch
from main import generate_member_resources


class TestGenerateMemberResources(unittest.TestCase):
    def setUp(self):
        self.team = {
            "name": "My Team",
            "members": [
                {"username": "alice", "role": "admin"},
                {"username": "bob", "role": "member"},
            ],
        }
        self.template = "templates/member.hcl"

    def test_generate_member_resources_with_members(self):
        expected = "alice admin resource\nbob member resource\n"
        read_template_mock = MagicMock(return_value="{member_name} {role} resource\n")
        with patch("main.read_template", read_template_mock):
            result = generate_member_resources(self.team)
            read_template_mock.assert_called_once_with(self.template)
            self.assertEqual(result, expected)

    def test_generate_member_resources_with_spaces_in_name(self):
        self.team["members"][0]["username"] = "Alice-Smith"
        expected = "Alice-Smith admin resource\nbob member resource\n"
        read_template_mock = MagicMock(return_value="{member_name} {role} resource\n")
        with patch("main.read_template", read_template_mock):
            result = generate_member_resources(self.team)
            read_template_mock.assert_called_once_with(self.template)
            self.assertEqual(result, expected)

    def test_generate_member_resources_with_custom_role(self):
        self.team["members"][1]["role"] = "editor"
        expected = "alice admin resource\nbob editor resource\n"
        read_template_mock = MagicMock(return_value="{member_name} {role} resource\n")
        with patch("main.read_template", read_template_mock):
            result = generate_member_resources(self.team)
            read_template_mock.assert_called_once_with(self.template)
            self.assertEqual(result, expected)
