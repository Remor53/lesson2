if __name__ == '__main__':
    friend_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    friend_name = friend_list[-1]
    while friend_name != "Валера" and len(friend_list) > 1:
        friend_list.pop()
        friend_name = friend_list[-1]
    if len(friend_list) > 1 or friend_list == ["Валера"]:
        print("Валера нашёлся")
    else:
        print("Валера нашёлся")

def find_person(name, flist):
    '''Ищет определённый объект в списке

    Ключевые аргументы:
    name -- объект, который необходимо найти в списке
    list -- список, в котором нужно искать

    Возвращает: текстовую строку (string)

    '''
    friend_name = flist[-1]
    while friend_name != name and len(flist) > 1:
        flist.pop()
        friend_name = flist[-1]
    if len(flist) > 1 or flist == [name]:
        return "Объект " + str(name) + " есть в списке"
    return "Объекта " + str(name) + " нет в списке"
