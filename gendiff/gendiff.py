import json
import yaml
import itertools

# def generate_diff(dict1, dict2):
#     res_dict = {**dict1, **dict2}
#     result = ['{', '\n']

#     for key in sorted(res_dict.keys()):
#         val1 = dict1.get(key)
#         val2 = dict2.get(key)

#         if val1 == val2:
#             if val1 is not None:
#                 result.append(f"    {key}: {str(val1).lower()}\n")
#         else:
#             result.append(f"  - {key}: {str(val1).lower()}\n"
#                           if val1 is not None else '')
#             result.append(f"  + {key}: {str(val2).lower()}\n"
#                           if val2 is not None else '')

#     result.append('}')
#     return ''.join(result)



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


def generate_diff(dict1, dict2, result={}):
    '''Функция принимает два словаря и возвращает один словарь, где в качестве ключей- кортеж, в который добавлены значения "add", "deleted" и "no_changed" в зависимости от различий переданных словарей
    '''
    res_dict = {**dict1, **dict2}
    for key in sorted(res_dict.keys()):
        val1 = dict1.get(key, 'incorrect')
        val2 = dict2.get(key, 'incorrect')

        if (isinstance(val1, dict) and isinstance(val2, dict)):
            children = {}
            result[(key, 'no_changed')] = generate_diff(val1, val2, children)

        else:
            if val1 == val2:
                result[(key, 'no_changed')] = val1

            else: #val1 != val2:
                if val1 != 'incorrect':
                    result[(key, 'deleted')] = val1
                if val2 != 'incorrect':
                    result[(key, 'added')] = val2

    return stylish(result)



    # res_dict = {**dict1, **dict2}
    # for key in sorted(res_dict.keys()):
    #     val1 = dict1.get(key)
    #     val2 = dict2.get(key)

    #     if not (isinstance(val1, dict) and isinstance(val2, dict)):
    #         if val1 == val2:
    #             if val1 is not None:
    #                 result[(key, 'no_changed')] = val1

    #         else: #val1 != val2:
    #             if val1 is not None:
    #                 result[(key, 'deleted')] = val1
    #             if val2 is not None:
    #                 result[(key, 'added')] = val2

    #     else:
    #         children = {}
    #         result[(key, 'no_changed')] = generate_diff(val1, val2, children)
                
    # return result


def stylish(data, replacer=' ', spaces_count=4):
    '''Функция принимает словарь и выводит его в формате, который нужен нам - с "+", "-", пробелами
    '''
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            if current_value is None:
                current_value = 'null'
            if type(current_value) == bool:
                current_value = str(current_value).lower()
            return str(current_value)
        
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if type(key) is tuple:
                a, b = key
                if b == 'deleted':
                    lines.append(f'{deep_indent}- {a}: {iter_(val, deep_indent_size)}')
                if b == 'added':
                    lines.append(f'{deep_indent}+ {a}: {iter_(val, deep_indent_size)}')
                if b == 'no_changed':
                    lines.append(f'{deep_indent}  {a}: {iter_(val, deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(data, 0)


    # str_data = ['{']
    # for k, v in data.items():
    #     if not isinstance(v, dict):

    #         if 'deleted' in  k:
    #             str_data.append(f'- {k[0]}: {str(v).lower()}')
    #         if 'added' in k:
    #             str_data.append(f'+ {k[0]}: {str(v).lower()}')
    #         if 'no_changed' in k:
    #             str_data.append(f'  {k[0]}: {str(v).lower()}')
    #     else:
    #         v = stylish(v, replacer, spaces_count)
    #         v = v.replace('\n', f'\n{replacer * spaces_count}')

            

    # result = f'\n{replacer * spaces_count}'.join(str_data) +'\n}'
    # return result


def converter(path):
    '''Функция, которая преобразует переданный путь до файла - json или yml - в словарь
    '''
    if '.json' in path:
        with open(path) as f:
            result = json.load(f)
    elif ('.yml' or '.yaml') in path:
        with open(path) as f:
            result = yaml.load(f, Loader=yaml.FullLoader)
    else:
        result = 'Please check the entered data. The function only works with .json and .yaml formats'
    return result


def take_args():
    '''Функция, которая берет аргументы из командной строки, возвращает два пути до файлов - уже реализована
    '''
    pass


# Итого общий результат следующий: stylish(different(converter(path1), converter(path2)))


def nested_json_diff():
    pass

def nested_yml_diff():
    pass
