import sys

import psycopg


#Подключаемся к postgresql
try:
    conn = psycopg.connect(dbname="TestTask", user="postgres", password="qwer1833", host="localhost", port="5432")
    cur = conn.cursor()
    print('Connected  OK')

except psycopg.DatabaseError as er:
    print('Connection failed', er)


#получаем из базы информацию по заказам , функция генератор
def take_order(arg):

    sql_from_order_product = cur.execute(
        f'''
        SELECT order_id, product_id, amount From order_product WHERE order_id IN ({arg})
        '''
    )
    result_from_order_product = sql_from_order_product.fetchall()

    for element in result_from_order_product:

        sql_from_product_shelf = cur.execute(
            f'''
                    SELECT  main_shelf,shelf_id FROM product_shelf WHERE product_id={element[1]} 
                    '''
        )
        result_from_product_shelf = sql_from_product_shelf.fetchall()

        sql_from_product = cur.execute(
            f'''
                   SELECT name FROM product WHERE id={element[1]}
                   '''
        )
        result_from_product = sql_from_product.fetchall()

        for_sql__from_shelf=', '.join([str(x[1]) for x in result_from_product_shelf])
        sql_from_shelf = cur.execute(
            f'''
                    SELECT id, name FROM shelf WHERE id IN ({for_sql__from_shelf})
                    '''
        )
        result_from_shelf = [list(x) for x in sql_from_shelf.fetchall()]

        for shelf in result_from_shelf:
            for pr_shelf in result_from_product_shelf:
                if shelf[0] == pr_shelf[1]:
                    shelf.append(pr_shelf[0])
        result_from_shelf.sort(key=lambda x: x[2], reverse=True)

        result = [element, result_from_product, *result_from_shelf]

        yield result




