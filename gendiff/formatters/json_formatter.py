import json


def json_format(diff):
    return json.dumps(get_dict(diff), indent=2)


def get_dict(diff_as_list):
    formatter = {}
    for item in diff_as_list:
        key, value = item['key'], item['value']
        action = item['action']
        if isinstance(value, list):
            formatter.setdefault(key, {
                "action": action,
                "value": get_dict(value)})
        elif isinstance(value, tuple):
            formatter.setdefault(key, {
                "action": action,
                "value": {
                    "old entry": value[0],
                    "new entry": value[1]}})
        else:
            formatter.setdefault(key, {
                "action": action,
                "value": value})
    return formatter
