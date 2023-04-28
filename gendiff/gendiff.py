import json
import yaml
import itertools


def make_diff(dict1, dict2, result={}):
    '''Функция принимает два словаря и возвращает один словарь, где в качестве ключей- кортеж, в который добавлены значения "add", "deleted" и "no_changed" в зависимости от различий переданных словарей
    '''
    res_dict = {**dict1, **dict2}
    for key in sorted(res_dict.keys()):
        val1 = dict1.get(key, 'incorrect')
        val2 = dict2.get(key, 'incorrect')

        if (isinstance(val1, dict) and isinstance(val2, dict)):
            children = {}
            result[(key, 'no_changed')] = make_diff(val1, val2, children)

        else:
            if val1 == val2:
                result[(key, 'no_changed')] = val1

            else: #val1 != val2:
                if val1 != 'incorrect':
                    result[(key, 'deleted')] = val1
                if val2 != 'incorrect':
                    result[(key, 'added')] = val2

    return result


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
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            sign = ''
            if type(key) is tuple:
                a, b = key
                if b == 'deleted':
                    sign = '- '

                if b == 'added':
                    sign = '+ '

                if b == 'no_changed':
                    sign = '  '
                key = a
    
            lines.append(f'{sign.rjust(deep_indent_size, replacer)}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(data, 0)


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


def generate_diff(path1, path2, formatter=stylish):
    return formatter(make_diff(converter(path1), converter(path2)))
