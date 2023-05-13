from itertools import chain


def stylish(data, replacer=' ', spaces_count=4, depth=0):
    '''Функция принимает словарь и выводит его в формате, который нужен нам - с "+", "-", пробелами
    '''
    if not isinstance(data, dict):
        if data is None:
            data = 'null'
        if type(data) == bool:
            data = str(data).lower()
        return str(data)
    
    current_indent = replacer * depth
    lines = []
    for key, val in data.items():
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

        lines.append(f'{sign.rjust(depth + spaces_count, replacer)}{key}: {stylish(val, replacer, spaces_count, (depth + spaces_count))}')
    result = chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
