import json

LEFT_BRACE = "{"
RIGHT_BRACE = "}"
INDENT = "    "
ADD = "  + "
DELETE = "  - "


def stylish_format(diff, depth=1):
    formatter = f"{LEFT_BRACE}\n"
    for item in diff:
        key, value = item['key'], normalize(item['value'], depth)
        action = item['action']
        if action == "nested":
            formatter += f"{indentor(depth, 'stay')}{key}: "
            formatter += f"{stylish_format(value, depth + 1)}\n"
        elif action == "added":
            formatter += f"{indentor(depth, 'add')}{key}: {value}\n"
        elif action == "deleted":
            formatter += f"{indentor(depth, 'del')}{key}: {value}\n"
        elif action == "updated":
            formatter += f"{indentor(depth, 'del')}{key}: {value[0]}\n"
            formatter += f"{indentor(depth, 'add')}{key}: {value[1]}\n"
        else:
            formatter += f"{indentor(depth, 'stay')}{key}: {value}\n"
    formatter += f"{indentor(depth - 1)}{RIGHT_BRACE}"
    return formatter


def normalize(raw_value, depth):
    if isinstance(raw_value, list):
        normalized_value = raw_value
    elif isinstance(raw_value, dict):
        normalized_value = f"{LEFT_BRACE}\n"
        normalized_value += get_tree(raw_value, depth + 1)
        normalized_value += f"{indentor(depth)}{RIGHT_BRACE}"
    elif isinstance(raw_value, tuple):
        normalized_value = (normalize(raw_value[0], depth),
                            normalize(raw_value[1], depth))
    else:
        normalized_value = json.dumps(raw_value).strip('"')
    return normalized_value


def get_tree(value, depth=0):
    tree = ""
    for nested_key, nested_value in value.items():
        if isinstance(nested_value, dict):
            tree += f"{indentor(depth)}{nested_key}: {LEFT_BRACE}\n"
            tree += f"{get_tree(nested_value, depth + 1)}"
            tree += f"{indentor(depth)}{RIGHT_BRACE}\n"
        else:
            nested_value = json.dumps(nested_value).strip('"')
            tree += f"{indentor(depth)}{nested_key}: {nested_value}\n"
    return tree


def indentor(depth, mode="stay"):
    if mode == "stay":
        return INDENT * depth
    elif mode == "add":
        return INDENT * (depth - 1) + ADD
    elif mode == "del":
        return INDENT * (depth - 1) + DELETE
