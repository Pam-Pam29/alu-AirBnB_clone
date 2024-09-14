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

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands:", output)

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            output = f.getvalue().strip()
            self.assertIn("No instance found with that ID", output)

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIn("Instance created successfully", output)

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234")
            output = f.getvalue().strip()
            self.assertIn("Instance deleted successfully", output)

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertIn("Instances found:", output)

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234 name 'New Name'")
            output = f.getvalue().strip()
            self.assertIn("Instance updated successfully", output)

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            output = f.getvalue().strip()
            self.assertIn("Unknown syntax:", output)

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_eof(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_base_model_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.all()")
            output = f.getvalue().strip()
            self.assertIn("Instances found:", output)

    def test_base_model_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            output = f.getvalue().strip()
            self.assertIn("Count:", output)

    def test_base_model_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show(1234)")
            output = f.getvalue().strip()
            self.assertIn("Instance found:", output)

    def test_base_model_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.destroy(1234)")
            output = f.getvalue().strip()
            self.assertIn("Instance deleted successfully", output)

    def test_base_model_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.update(1234, 'name', 'New Name')")
            output = f.getvalue().strip()
            self.assertIn("Instance updated successfully", output)

    def test_user_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertIn("Instances found:", output)

    def test_user_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertIn("Count:", output)

    def test_user_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show(1234)")
            output = f.getvalue().strip()
            self.assertIn("Instance found:", output)

    def test_user_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.destroy(1234)")
            output = f.getvalue().strip()
            self.assertIn("Instance deleted successfully", output)

    def test_user_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.update(1234, 'name', 'New Name')")
            output = f.getvalue().strip()
            self.assertIn("Instance updated successfully", output)

    def test_state_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.all()")
            output = f.getvalue().strip()
            self.assertIn("Instances found:", output)

    def test_state_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.count()")
            output = f.getvalue().strip()
            self.assertIn("Count:", output)

    def test_state_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.show(1234)")
            output = f.getvalue().strip()
            self.assertIn("Instance found:", output)

    def test_state_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.destroy(1234)")
            output = f.getvalue().strip()
            self.assertIn("Instance deleted successfully", output)

    def test_state_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.update(1234, 'name', 'New Name')")
            output = f.getvalue().strip()
            self.assertIn("Instance updated successfully", output)

    def test_city_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.all()")
            output = f.getvalue().strip()
            self.assertIn("Instances found:", output)

    def test_city_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.count()")
            output = f.getvalue().strip()
            self.assertIn("Count:", output)

    def test_city_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.show(1234)")
            output = f.getvalue().strip()
            self.assertIn("Instance found:", output)

    def test_city_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.destroy(1234)")
            output = f.getvalue().strip()
            self.assertIn("Instance deleted successfully", output)

    def test_city_update(self):
        with patch('sys.stdout', new=StringIO()) as
