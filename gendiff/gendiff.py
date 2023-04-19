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
    with open(pos1) as f1, open(pos2) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)

    res_dict = {**file1, **file2}
    result = ['{', '\n']

    for key in sorted(res_dict.keys()):
        val1 = file1.get(key)
        val2 = file2.get(key)

        if val1 == val2:
            if val1 is not None:
                result.append(f"    {key}: {str(val1).lower()}\n")
        else:
            result.append(f"  - {key}: {str(val1).lower()}\n"
                          if val1 is not None else '')
            result.append(f"  + {key}: {str(val2).lower()}\n"
                          if val2 is not None else '')

    result.append('}')
    return ''.join(result)
