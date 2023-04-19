import json
import yaml


def generate_diff(dict1, dict2):
    res_dict = {**dict1, **dict2}
    result = ['{', '\n']

    for key in sorted(res_dict.keys()):
        val1 = dict1.get(key)
        val2 = dict2.get(key)

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


def plain_json_diff(pos1, pos2):
    with open(pos1) as f1, open(pos2) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)
    return generate_diff(file1, file2)


def plain_yml_diff(pos1, pos2):
    with open(pos1) as f1, open(pos2) as f2:
        file1 = yaml.load(f1, Loader=yaml.FullLoader)
        file2 = yaml.load(f2, Loader=yaml.FullLoader)
    return generate_diff(file1, file2)
