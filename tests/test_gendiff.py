import pytest
from gendiff import generate_diff

@pytest.fixture()
def plain_files_test():
    with open('./tests/fixtures/plain_files_test.txt', encoding='utf-8') as f:
        result = f.read().strip()
    return result


@pytest.fixture()
def nested_files_test():
    with open('./tests/fixtures/nested_files_test.txt', encoding='utf-8') as f:
        result = f.read().strip()
    return result


def test_generate_diff_plain_json(plain_files_test):
    assert generate_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.json") == plain_files_test, 'JSON plain test dropped'


def test_generate_diff_plain_yaml(plain_files_test):
    assert generate_diff("./tests/fixtures/file1.yml", "./tests/fixtures/file2.yml") == plain_files_test, 'YAML plain test dropped'


def test_generate_diff_nested_json(nested_files_test):
    assert generate_diff("./tests/fixtures/file1_nested.json", "./tests/fixtures/file2_nested.json") == nested_files_test, 'JSON nested test dropped'
    
    
def test_generate_diff_nested_yaml(nested_files_test):
    assert generate_diff("./tests/fixtures/file1_nested.yml", "./tests/fixtures/file2_nested.yml") == nested_files_test, 'YAML nested test dropped'


# ниже применение фикстур с параметрами от chatGPT
# import pytest
# from gendiff import generate_diff

# @pytest.fixture(params=[
#     ('./tests/fixtures/file1.json', './tests/fixtures/file2.json', 'plain_files_test.txt', 'JSON plain test dropped'),
#     ('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml', 'plain_files_test.txt', 'YAML plain test dropped'),
#     ('./tests/fixtures/file1_nested.json', './tests/fixtures/file2_nested.json', 'nested_files_test.txt', 'JSON nested test dropped'),
#     ('./tests/fixtures/file1_nested.yml', './tests/fixtures/file2_nested.yml', 'nested_files_test.txt', 'YAML nested test dropped'),
# ])
# def file_params(request):
#     with open(f'./tests/fixtures/{request.param[2]}', encoding='utf-8') as f:
#         result = f.read().strip()
#     return request.param[:2], result, request.param[3]

# def test_generate_diff(file_params):
#     files, expected, message = file_params
#     assert generate_diff(files[0], files[1]) == expected, message
