import re
import pytest

pattern = r"(\w+[aeoiu]\w*ing)|(\w+[^aeiouy]y\w*ing)|([^aeoiu\s]y\w*ing)"

test_cases = [("doing", True),
              ("lying", True),
              ("ying", False),
              ("trying", True),
              ("covering", True),
              ("sting", False),
              ("ring", False),
              ("lowering", True),
              (" Doing sports is highly beneficial for your health.", True)
              ]


@pytest.mark.parametrize("string,matches", test_cases)
def test_gerund_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.search(pattern, string) is not None) == matches
