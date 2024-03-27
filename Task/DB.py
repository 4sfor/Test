import psycopg


#Подключаемся к postgresql
def connect_to_db():
    try:
        conn = psycopg.connect(dbname="TestTask", user="postgres", password="qwer1833", host="localhost", port="5432")
        print('Connected  OK')
        return conn
    except psycopg.DatabaseError as er:
        print('Connection failed', er)


#получаем из базы информацию по заказам
def take_order(args):
    conn = connect_to_db()
    cur = conn.cursor()
    args_unpacking = ", ".join(args)
    resultSQL = cur.execute(
        f'''
        SELECT order_product.order_id, order_product.product_id , order_product.amount, product_shelf.main_shelf,  product.name, shelf.name FROM 
        order_product INNER JOIN product_shelf ON order_product.product_id = product_shelf.product_id INNER JOIN 
        product ON order_product.product_id = product.id INNER JOIN shelf ON product_shelf.shelf_id=shelf.id WHERE order_product.order_id IN ({args_unpacking}) ORDER BY shelf.name
        '''
    )
    result = [list(x)for x in resultSQL.fetchall()]
    for element in result:
        if element[3]:
            for elem in result:
                if element[0:2] == elem[0:2] and elem[3] != element[3]:
                    element.append(elem[5])
                    result.remove(elem)
        else:
            continue

    return result


