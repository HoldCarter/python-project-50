import argparse
import json


def generate_diff():
    parser = argparse.ArgumentParser(description="Compares two configuration \
                                      files and shows a difference.")
    parser.add_argument('first_file', type=str, help='First file to compare')
    parser.add_argument('second_file', type=str, help='Second file to compare')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file1 = json.load(open(f'{args.first_file}'))
    file2 = json.load(open(f'{args.second_file}'))
    result = ''
    for key in sorted(set(file1.keys()) | set(file2.keys())):
        if file1.get(key) != file2.get(key):
            if file1.get(key) or file1.get(key) is False:
                result += f"- {key}: {file1.get(key)}\n"
            if file2.get(key):
                result += f"+ {key}: {file2.get(key)}\n"
        else:
            result += f"  {key}: {file1.get(key)}\n"
    result = result[:-1]
    print(result)

# gendiff ./data/file1.json ./data/file2.json
