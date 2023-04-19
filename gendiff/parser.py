import argparse


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
