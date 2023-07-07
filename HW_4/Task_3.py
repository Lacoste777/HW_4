# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def elements(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[str(value)] = key
    return result


print(elements(two=15, one=32.1, ten='Hello world!', four='4'))