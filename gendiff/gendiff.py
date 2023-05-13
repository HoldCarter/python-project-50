from gendiff.formatters import plain_format, json_format, stylish_format
from gendiff.diff import make_diff
from gendiff.parser import converter


FORMATTERS = {
    "stylish": stylish_format,
    "plain": plain_format,
    "json": json_format
}


def generate_diff(path1, path2, formatter="stylish"):
    formatter = FORMATTERS[formatter]
    result = formatter(make_diff(converter(path1), converter(path2)))
    return result
