"""Tests for `devtools.cli.main_cli` module.

These tests are for the custom behavior of the devtools cli.
"""

from click.testing import CliRunner
from devtools.cli import main_cli as cli

# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert "Console script for devtools" in result.output
#     help_result = runner.invoke(cli.main, ["--help"])
#     assert help_result.exit_code == 0
#     assert "Show this message and exit." in help_result.output

# def test_hello():
#     """Test the hello command."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main, ["hello", "Foo"])
#     assert result.exit_code == 0
#     assert "Hello Foo" in result.output
#     help_result = runner.invoke(cli.main, ["--help"])
#     assert help_result.exit_code == 0
#     assert "--help  Show this message and exit." in help_result.output
