from Task.result_from_db import get_result
import psycopg


# Подключаемся к postgresql
def connect_to_db():
    try:
        conn = psycopg.connect(dbname="TestTask", user="postgres", password="qwer1833", host="localhost", port="5432")
        cursor = conn.cursor()
        print('Connected  OK')
        return cursor
    except psycopg.DatabaseError as er:
        print('Connection failed', er)


# получаем из базы информацию по заказам
def take_order(args):
    cur = connect_to_db()
    number = ', '.join(args)
    sql_from_order_product = cur.execute(
        f'''
        SELECT order_id, product_id, amount From order_product WHERE order_id IN ({number})
        '''
    )
    result_from_order_product = sql_from_order_product.fetchall()

    a = ', '.join(str(x[1]) for x in result_from_order_product)

    sql_from_product = cur.execute(
        f'''
           SELECT name, id  FROM product WHERE id IN ({a})
           '''
    )

    result_from_product = sql_from_product.fetchall()


    sql_from_product_shelf = cur.execute(
        f'''
                    SELECT  main_shelf,shelf_id, product_id FROM product_shelf WHERE product_id IN ({a}) 
            '''
    )

    result_from_product_shelf = [list(x) for x in sql_from_product_shelf.fetchall()]


    b = ', '.join(str(x[1]) for x in result_from_order_product)
    sql_from_shelf = cur.execute(
        f'''
                SELECT id, name FROM shelf WHERE id IN ({b})
            '''
    )
    result_from_shelf = sql_from_shelf.fetchall()

    return get_result(result_from_order_product, result_from_product, result_from_product_shelf, result_from_shelf)



