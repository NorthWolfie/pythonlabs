import sqlite3

import pandas as pd

if __name__ == '__main__':
    path = 'C:/Users/guy20/Desktop/Python_Labs/pythonProject/lab4/orders.csv'
    columns = ["user_id", "order_id", "order_time", "order_cost", "success_order_flg"]
    db = sqlite3.connect(path)
    cur = db.cursor()
    orders = pd.read_csv(path, delimiter=';')
    orders['order_time'] = pd.to_datetime(orders['order_time'], unit='s', errors='coerce')
    orders['order_cost'] = pd.to_numeric(orders['order_cost'], errors='coerce')
    orders.dropna()
    orders.to_sql('orders', db, index=False)
    table = cur.execute("SELECT * FROM orders LIMIT 6").fetchall()
    df = pd.DataFrame(table, columns=columns).style.hide(axis='index')

    """
    input_cur.execute("SELECT MIN(order_time)
    FROM orders
    WHERE 
    ")

    output_db = sqlite3.connect('result.csv')
    output_cur = output_db.cursor()
    output_cur.execute("CREATE TABLE IF NOT EXISTS result(
        date INT,
        gmv360d_new REAL,
        gmv360d_reactivated REAl,
        users_count_new INT,
        users_count_reactivated INT);
        ")
    output_db.commit()
    """
