from gendiff import take_args, plain_yml_diff, plain_json_diff


def main():
    first_file, second_file = take_args()
    if '.json' in first_file:
        print(plain_json_diff(first_file, second_file))
    else:
        print(plain_yml_diff(first_file, second_file))


if __name__ == '__main__':
    main()
