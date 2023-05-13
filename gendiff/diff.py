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