def str_check(str1, str2):
    '''Проверяет объекты на пренадлежность типу string.
    Если оба объекта строки, то проверяет одинаковые ли они,
    если разные, то определяет какая длиннее и проверяет, является
    ли вторая строка словом 'learn'

    Ключевые аргументы:
    str1 -- первый объект
    str2 -- второй объект

    Возвращает: различные целые числовые значения (int), 
    либо кортеж из двух чисел (tuple)

    '''
    type1 = str(type(str1))
    type2 = str(type(str2))
    if type1 != '<class \'str\'>' or type2 != '<class \'str\'>':
        return 0
    elif len(str1) == len(str2):
        return 1
    elif len(str1) > len(str2):
        if str2 == 'learn':
            return 2, 3
        else:
            return 2
    elif str2 == 'learn':
        return 3
        
if __name__ == '__main__':
    print(str_check(1, 3))
    print(str_check('hello', 'hello'))
    print(str_check('good morning', 'hello'))
    print(str_check('learning', 'learn'))
    print(str_check('read', 'learn'))