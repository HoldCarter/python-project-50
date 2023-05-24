def make_diff(contents1, contents2):
    keys_common = sorted(set(contents1.keys()) | set(contents2.keys()))
    diff = []
    for key in keys_common:
        value1 = contents1.get(key, "!none")
        value2 = contents2.get(key, "!none")
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(item(key, make_diff(value1, value2), "nested"))
        elif value1 == value2:
            diff.append(item(key, value1, "unchanged"))
        elif value2 == "!none":
            diff.append(item(key, value1, "deleted"))
        elif value1 == "!none":
            diff.append(item(key, value2, "added"))
        else:
            diff.append(item(key, (value1, value2), "updated"))
    return diff


def item(key, value, action):
    return {
        "key": key,
        "value": value,
        "action": action}
