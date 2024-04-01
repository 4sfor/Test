
def get_result(result_from_order_product, result_from_product, result_from_product_shelf, result_from_shelf):
    result = []
    for order in result_from_order_product:
        for product in result_from_product:
            if order[1] in product:
                result.append([order, product])

    for pr_shelf in result_from_product_shelf:
        for shelf in result_from_shelf:
            if pr_shelf[1] == shelf[0]:
                pr_shelf.append(shelf[1])


    for element in result:
        element.append([])
        for product_shelf in result_from_product_shelf:
            if element[1][1] == product_shelf[2]:
                element[2].append(product_shelf)
        element[2].sort(key=lambda x: x[0], reverse=True)


    return result
