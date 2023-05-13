import json
import yaml
from gendiff.formatters import stylish
from gendiff.diff import make_diff
from gendiff.parser import converter


FORMATTERS = {
    "stylish": stylish
    # "plain": plain_format,
    # "json": json_format
}


def generate_diff(path1, path2, formatter="stylish"):
    formatter = FORMATTERS[formatter]
    result = formatter(make_diff(converter(path1), converter(path2)))
    return result