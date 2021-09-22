import re
import pytest
from itertools import chain

pattern = r"(\(\?[^:=!<].*?\))|(\([^\?].*?\))"

test_cases = [
    ("back(boards|block)", ["(boards|block)"]),
    ("(?:non-capturing)(capturing group)", ["(capturing group)"]),
    ("(\w+)(?=\d)", ["(\w+)"]),
    ("(?P<year>\d{4})-(?P<month>\d{2})(?! [a-z])", ["(?P<year>\d{4})", "(?P<month>\d{2})"]),
    ("(?<=[A-Z])1234 teach(er|ing)", ["(er|ing)"]),
    ("(?<!\d)", [None]),
    ("(?P=name\w+)", ["(?P=name\w+)"])
]


@pytest.mark.parametrize("string, answer", test_cases)
def test_group_capturing(string, answer):
    """Test whether pattern correctly matches or does not match input."""
    nested_list = [[x for x in y if len(x) != 0] for y in re.findall(pattern, string)]
    flat_list = list(chain(*nested_list))
    s = zip(flat_list, answer)
    for el in s:
        print(el)
        assert el[0] == el[1]
