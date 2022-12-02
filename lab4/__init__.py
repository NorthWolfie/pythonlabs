import sqlite3




if __name__ == '__main__':
    input_db = sqlite3.connect('orders.csv')
    input_cur = input_db.cursor()
    input_cur.execute("""CREATE TABLE IF NOT EXISTS orders(
       user_id TEXT PRIMARY KEY,
       order_id TEXT,
       order_time INT,
       order_cost REAL,
       success_order_flg BOOlEAN);
    """)

    output_db = sqlite3.connect('result.csv')
    output_cur = output_db.cursor()
    output_cur.execute("""CREATE TABLE IF NOT EXISTS result(
        date INT,
        gmv360d_new REAL,
        gmv360d_reactivated REAl,
        users_count_new INT,
        users_count_reactivated INT);
        """)
    output_db.commit()
