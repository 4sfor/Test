from Task.DB import take_order


#Получить ввод пользователя
def take_number_orders():
    numbers = input("Введите номера заказов через пробел: ").split()
    return numbers


#Получение товаров на стеллажах
def take_shelf():
    data_from_db = take_order(take_number_orders())

    shelf = {}
    for element in data_from_db:
        shelf[element[5]] = [elem for elem in data_from_db if element[5] == elem[5]]
    sorted_shelf = dict(sorted(shelf.items()))

    return sorted_shelf


#Вывод в консоль
def output():
    dict_result = take_shelf()
    for element in dict_result:
        print(f'===Стеллаж {element}')
        for element_shelf in dict_result[element]:
            if len(element_shelf) > 6:
                print(f'{element_shelf[4]} (id={element_shelf[1]})\nзаказ {element_shelf[0]}, {element_shelf[2]} шт\n'
                      f'доп стеллаж: {",".join(element_shelf[6:])}\n')
            else:
                print(f'{element_shelf[4]} (id={element_shelf[1]})\nзаказ {element_shelf[0]}, {element_shelf[2]} шт\n')



output()
