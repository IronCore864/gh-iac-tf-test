import unittest
from unittest.mock import MagicMock, patch
from main import generate_team_resource


class TestGenerateTeamResource(unittest.TestCase):
    def setUp(self):
        self.team = {"name": "My Team", "description": "A test team"}
        self.parent = "parent_team"
        self.child_template = "templates/team-child.hcl"
        self.parent_template = "templates/team-parent.hcl"

    def test_generate_team_resource_with_parent(self):
        expected = "child team resource"
        read_template_mock = MagicMock(return_value=expected)
        with patch("main.read_template", read_template_mock):
            result = generate_team_resource(self.team, self.parent)
            read_template_mock.assert_called_once_with(self.child_template)
            self.assertEqual(result, expected)

    def test_generate_team_resource_without_parent(self):
        expected = "parent team resource"
        read_template_mock = MagicMock(return_value=expected)
        with patch("main.read_template", read_template_mock):
            result = generate_team_resource(self.team, None)
            read_template_mock.assert_called_once_with(self.parent_template)
            self.assertEqual(result, expected)

    def test_generate_team_resource_with_spaces_in_name(self):
        self.team["name"] = "My Test Team"
        expected = "parent team resource"
        read_template_mock = MagicMock(return_value=expected)
        with patch("main.read_template", read_template_mock):
            result = generate_team_resource(self.team, None)
            read_template_mock.assert_called_once_with(self.parent_template)
            self.assertEqual(result, expected)

    def test_generate_team_resource_with_unicode_in_name(self):
        self.team["name"] = "My Team"
        expected = "parent team resource"
        read_template_mock = MagicMock(return_value=expected)
        with patch("main.read_template", read_template_mock):
            result = generate_team_resource(self.team, None)
            read_template_mock.assert_called_once_with(self.parent_template)
            self.assertEqual(result, expected)

    def test_generate_team_resource_with_unicode_in_description(self):
        self.team["description"] = "A test team"
        expected = "parent team resource"
        read_template_mock = MagicMock(return_value=expected)
        with patch("main.read_template", read_template_mock):
            result = generate_team_resource(self.team, None)
            read_template_mock.assert_called_once_with(self.parent_template)
            self.assertEqual(result, expected)
