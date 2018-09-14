def purpose_determination(user_age):
    '''Определяет по возрасту пользователя, чем он должен заниматься: 
    учиться в детском саду, школе, ВУЗе или работать

    Ключевые аргументы: 
    user_age -- возраст пользователя

    Возвращает: текстовую строку (string)

    '''
    if user_age < 1:
        return 'Возвраст пользователя введён некорректно'
    elif user_age < 3:
        purpose = 'Пользователь ещё младенец'
    elif user_age < 7:
        purpose = 'Пользователь ходит в детский сад'
    elif user_age < 19:
        purpose = 'Пользователь учится в школе'
    elif user_age < 23:
        purpose = 'Пользователь учится в ВУЗе'
    else:
        purpose = 'Пользователь работает'
    return purpose

if __name__ == '__main__':
    age = int(input('Введите ваш возвраст: '))
    check = purpose_determination(age)
    print(check)
