"""Test name-matching regular expression."""
import re
import pytest

# vvv ADD YOUR PATTERN HERE vvv #
pattern = r"[A-Z][a-z\.]+(( [A-Z][-\w,\.]+)+|( [a-z]+ [A-Z][a-z]+)+)"
# ^^^ ADD YOUR PATTERN HERE ^^^ #
# raise NotImplementedError("Add your pattern to the test file.")


test_cases = [
    ("Quan Hongchan", True),
    ("Philip Seymour Hoffman", True),
    ("Dr. Nicki Washington", True),
    ("Joseph Gordon-Levitt", True),
    ("Ken Griffey, Jr.", True),
    ("John von Neumann", True),
    ("Cher", False),
    ("not a name", False),
    ("happy feet", False),
    ("The end", False),
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_name_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.fullmatch(pattern, string) is not None) == matches
