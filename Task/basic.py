from Task.DB import take_order


#Получить ввод пользователя
def take_number_orders():
    numbers = input("Введите номера заказов через пробел: ").split()
    return numbers


#Получение товаров на стеллажах
def take_shelf():
    shelf = {}
    for number in take_number_orders():
        for element in take_order(number):
            key = element[2][1]
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

            if len(element_shelf) > 3:
                print(f'{element_shelf[1][0][0]} (id={element_shelf[0][1]})\nзаказ {element_shelf[0][0]}, {element_shelf[0][2]} шт\n'
                      f'доп стеллаж: {",".join([x[1] for x in element_shelf[3:]])}\n')
            else:
                print(f'{element_shelf[1][0][0]} (id={element_shelf[0][1]})\nзаказ {element_shelf[0][0]}, {element_shelf[0][2]} шт\n')





output()

