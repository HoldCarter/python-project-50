import pytest
import os
from gendiff import generate_diff

# @pytest.fixture()
# def plain_files_test():
#     with open('tests/fixtures/plain_files_test.txt', encoding='utf-8') as f:
#         result = f.read().strip()
#     return result


# @pytest.fixture()
# def nested_files_test():
#     with open('tests/fixtures/nested_files_test.txt', encoding='utf-8') as f:
#         result = f.read().strip()
#     return result


# def test_generate_diff_plain_json(plain_files_test):
#     assert generate_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json") == plain_files_test, 'JSON plain test dropped'


# def test_generate_diff_plain_yaml(plain_files_test):   
#     assert generate_diff("./tests/fixtures/file1.yml", "./tests/fixtures/file2.yml") == plain_files_test, 'YAML plain test dropped'


# def test_generate_diff_nested_json(nested_files_test):
#     assert generate_diff("./tests/fixtures/file1_nested.json", "./tests/fixtures/file2_nested.json") == nested_files_test, 'JSON nested test dropped'


# def test_generate_diff_nested_yaml(nested_files_test):    
#     assert generate_diff("./tests/fixtures/file1_nested.yml", "./tests/fixtures/file2_nested.yml") == nested_files_test, 'YAML nested test dropped'    
    


test_cases = [
    # ("file1.json", "file2.json", "plain_files_test.txt", "stylish"),
    # ("file1.yml", "file2.yml", "plain_files_test.txt", "stylish"),
    ("file1_nested.json", "file2_nested.json", "nested_files_test.txt", "stylish"),
    ("file1_nested.yml", "file2_nested.yml", "nested_files_test.txt", "stylish")
    # ("file1.json", "file2.json", "expected/simple_plain.txt", "plain"),
    # ("file1.yaml", "file2.yaml", "expected/simple_plain.txt", "plain"),
    # ("file1_nested.json", "file2_nested.json", "expected/nested_plain.txt", "plain"),
    # ("file1_nested.yaml", "file2_nested.yaml", "expected/nested_plain.txt", "plain"),
    # ("file1.json", "file2.json", "expected/simple_json.txt", "json"),
    # ("file1.yaml", "file2.yaml", "expected/simple_json.txt", "json"),
    # ("file1_nested.json", "file2_nested.json", "expected/nested_json.txt", "json"),
    # ("file1_nested.yaml", "file2_nested.yaml", "expected/nested_json.txt", "json")
]


def get_fixture_path(local_filename):
    return os.path.join('tests/fixtures', local_filename)


@pytest.mark.parametrize("file1, file2, expected, formatter", test_cases)
def test_universal_case(file1, file2, expected, formatter):
    with open(get_fixture_path(expected), 'r') as result:
        # result_content = "\n".join(result.read().splitlines())
        result_content = result.read().strip()
    assert generate_diff(
        get_fixture_path(file1),
        get_fixture_path(file2),
        formatter) == result_content
