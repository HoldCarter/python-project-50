import argparse
import json


def take_args():
    parser = argparse.ArgumentParser(description="Compares two configuration \
                                      files and shows a difference.")
    parser.add_argument('first_file', type=str, help='First file to compare')
    parser.add_argument('second_file', type=str, help='Second file to compare')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file_path = args.first_file
    second_file_path = args.second_file
    return first_file_path, second_file_path


def generate_diff(pos1, pos2):
    file1 = json.load(open(f'{pos1}'))
    file2 = json.load(open(f'{pos2}'))
    result = ''  # требование, чтобы результатом была строка
    res_dict = {**file1, **file2}
    for key in sorted(res_dict.keys()):
        if file1.get(key) != file2.get(key):
            if file1.get(key) is not None:
                result += f"  - {key}: {str(file1.get(key)).lower()}\n"
            if file2.get(key) is not None:
                result += f"  + {key}: {str(file2.get(key)).lower()}\n"
        else:
            result += f"    {key}: {str(file1.get(key)).lower()}\n"
    result = "{" + "\n" + result[:-1] + "\n" + "}"
    return result

# gendiff ./data/file1.json ./data/file2.json
