from gendiff import generate_diff, take_args


def main():
    first_file, second_file = take_args()
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
