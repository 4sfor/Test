from Task.DB import take_order

import time
#Получить ввод пользователя
def take_number_orders():
    numbers = input("Введите номера заказов через пробел: ").split()
    return numbers


#Получение товаров на стеллажах
def take_shelf():
    shelf = {}
    for element in take_order(take_number_orders()):
        key = element[2][0][1]
        if key not in shelf:
            shelf[key] = []
        shelf[key].append(element)
    sorted_shelf = dict(sorted(shelf.items()))
    return sorted_shelf


#Вывод в консоль
def output():
    dict_result = take_shelf()
    for key in dict_result:
        print(f'===Стеллаж {key}')
        for element_shelf in dict_result[key]:
            if len(element_shelf[2]) > 1:
                print(f'{element_shelf[1][0]} (id={element_shelf[1][1]})\nзаказ {element_shelf[0][0]}, {element_shelf[0][1]} шт\n'
                      f'доп стеллаж: {",".join([x[-1] for x in element_shelf[2][1:]])}\n')
            else:
                print(f'{element_shelf[1][0]} (id={element_shelf[1][1]})\nзаказ {element_shelf[0][0]}, {element_shelf[0][1]} шт\n')





output()

