#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNBCommand console."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test that empty line does not execute any command."""
        console = HBNBCommand()
        console.onecmd("")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test quit command to exit the program."""
        console = HBNBCommand()
        self.assertTrue(console.onecmd("quit"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """Test EOF command to exit the program."""
        console = HBNBCommand()
        self.assertTrue(console.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class(self, mock_stdout):
        """Test create command with no class name."""
        console = HBNBCommand()
        console.onecmd("create")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        """Test create command with invalid class name."""
        console = HBNBCommand()
        console.onecmd("create InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_valid_class(self, mock_stdout):
        """Test create command with valid class name."""
        console = HBNBCommand()
        with patch('models.storage.save'):
            console.onecmd("create User")
        output = mock_stdout.getvalue().strip()
        self.assertRegex(output, r'[a-f0-9-]+')

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        """Test show command with missing class name."""
        console = HBNBCommand()
        console.onecmd("show")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        """Test show command with invalid class name."""
        console = HBNBCommand()
        console.onecmd("show InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_id(self, mock_stdout):
        """Test show command with missing id."""
        console = HBNBCommand()
        console.onecmd("show User")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_no_instance_found(self, mock_stdout):
        """Test show command with non-existent id."""
        console = HBNBCommand()
        console.onecmd("show User 1234-5678")
        self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        """Test destroy command with missing class name."""
        console = HBNBCommand()
        console.onecmd("destroy")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class(self, mock_stdout):
        """Test destroy command with invalid class name."""
        console = HBNBCommand()
        console.onecmd("destroy InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_id(self, mock_stdout):
        """Test destroy command with missing id."""
        console = HBNBCommand()
        console.onecmd("destroy User")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_no_instance_found(self, mock_stdout):
        """Test destroy command with non-existent id."""
        console = HBNBCommand()
        console.onecmd("destroy User 1234-5678")
        self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_invalid_class(self, mock_stdout):
        """Test all command with invalid class name."""
        console = HBNBCommand()
        console.onecmd("all InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_invalid_class(self, mock_stdout):
        """Test count command with invalid class name."""
        console = HBNBCommand()
        console.onecmd("count InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        """Test update command with missing class name."""
        console = HBNBCommand()
        console.onecmd("update")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class(self, mock_stdout):
        """Test update command with invalid class name."""
        console = HBNBCommand()
        console.onecmd("update InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_id(self, mock_stdout):
        """Test update command with missing id."""
        console = HBNBCommand()
        console.onecmd("update User")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_no_instance_found(self, mock_stdout):
        """Test update command with non-existent id."""
        console = HBNBCommand()
        console.onecmd("update User 1234-5678")
        self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    # Additional tests can be added for advanced functionality like:
    # - Update with dictionaries
    # - Testing the all method for specific class filtering
    # - Testing command formats like <class>.show(<id>)


if __name__ == "__main__":
    unittest.main()
