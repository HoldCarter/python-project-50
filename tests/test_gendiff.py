import pytest
from gendiff import generate_diff, take_args


def test_generate_diff():
    plain_test_path = 'fixtures/plain_files_test.txt'
    with open(plain_test_path, encoding='utf8') as f:
        plain_test = f.read().strip()
        assert generate_diff("fixtures/file1.json", "fixtures/file2.json") == plain_test
