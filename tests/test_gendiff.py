import pytest
from gendiff import plain_yml_diff, plain_json_diff



@pytest.fixture
def plain_files_test():
    with open('./tests/fixtures/plain_files_test.txt', encoding='utf-8') as f:
        return f.read().strip()


@pytest.fixture
def nested_files_test():
    with open('./tests/fixtures/nested_files_test.txt', encoding='utf-8') as f:
        return f.read().strip()


def test_plain_json_diff(plain_files_test):
    assert plain_json_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json") == plain_files_test, 'JSON plain test dropped'


def test_plain_yml_diff(plain_files_test):
    assert plain_yml_diff("./tests/fixtures/file1.yml", "./tests/fixtures/file2.yml") == plain_files_test, 'YML plain test dropped'


# def test_nested_json_diff(nested_files_test):
#     assert nested_json_diff("./tests/fixtures/file1_nested.json", "./tests/fixtures/file2_nested.json") == nested_files_test, 'JSON nested test dropped'


# def test_nested_yml_diff(nested_files_test):
#     assert nested_yml_diff("./tests/fixtures/file1_nested.yml", "./tests/fixtures/file2_nested.yml") == nested_files_test, 'YML nested test dropped'