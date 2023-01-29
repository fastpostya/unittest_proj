def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует. В ином случае возвращается значение default.
    :param collection: словарь с исходными данными
    :param key:
    :param default:
    :return:
    """
    if key in collection:
        return collection[key]
    else:
        return default
