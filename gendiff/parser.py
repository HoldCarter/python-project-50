import argparse
import json
import yaml


def take_args():
    parser = argparse.ArgumentParser(description="Compares two configuration \
                                      files and shows a difference.")
    parser.add_argument('first_file', type=str, help='First file to compare')
    parser.add_argument('second_file', type=str, help='Second file to compare')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')

    args = parser.parse_args()
    first_file_path = args.first_file
    second_file_path = args.second_file
    formatter = args.format
    return first_file_path, second_file_path, formatter


def converter(file):
    if file.endswith(".json"):
        loader = json.load
    elif file.endswith((".yaml", ".yml")):
        loader = yaml.safe_load
    else:
        raise Exception("Please check the entered data. The function only works with .json and .yaml formats")

    with open(file) as current_file:
        return loader(current_file)
