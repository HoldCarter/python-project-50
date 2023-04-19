import pytest
from gendiff import plain_yml_diff, plain_json_diff,generate_diff



@pytest.fixture
def plain_files_test():
    return './tests/fixtures/plain_files_test.txt'


def test_plain_json_diff(plain_files_test):
    with open(plain_files_test, encoding='utf8') as f:
        plain_test = f.read().strip()
        
    assert plain_json_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json") == plain_test, 'JSON test dropped'


def test_plain_yml_diff(plain_files_test):
    with open(plain_files_test, encoding='utf8') as f:
        plain_test = f.read().strip()


    assert plain_yml_diff("./tests/fixtures/file1.yml", "./tests/fixtures/file2.yml") == plain_test, 'YML test dropped'
