import pytest
import os
from gendiff import generate_diff


test_cases = [
    ("file1.json", "file2.json", "simple_stylish.txt", "stylish"),
    ("file1.yaml", "file2.yaml", "simple_stylish.txt", "stylish"),
    ("file1_nested.json", "file2_nested.json", "nested_stylish.txt", "stylish"),
    ("file1_nested.yaml", "file2_nested.yaml", "nested_stylish.txt", "stylish"),
    ("file1.json", "file2.json", "simple_plain.txt", "plain"),
    ("file1.yaml", "file2.yaml", "simple_plain.txt", "plain"),
    ("file1_nested.json", "file2_nested.json", "nested_plain.txt", "plain"),
    ("file1_nested.yaml", "file2_nested.yaml", "nested_plain.txt", "plain"),
    ("file1.json", "file2.json", "simple_json.txt", "json"),
    ("file1.yaml", "file2.yaml", "simple_json.txt", "json"),
    ("file1_nested.json", "file2_nested.json", "nested_json.txt", "json"),
    ("file1_nested.yaml", "file2_nested.yaml", "nested_json.txt", "json")
]


def get_fixture_path(local_filename):
    return os.path.join('tests/fixtures', local_filename)


@pytest.mark.parametrize("file1, file2, expected, formatter", test_cases)
def test_universal_case(file1, file2, expected, formatter):
    with open(get_fixture_path(expected), 'r') as result:
        result_content = "\n".join(result.read().splitlines())
    assert generate_diff(
        get_fixture_path(file1),
        get_fixture_path(file2),
        formatter) == result_content
