import sqlite3
import plotly.graph_objects as go
import pandas as pd

if __name__ == '__main__':
    path = 'C:/Users/guy20/Desktop/Python_Labs/pythonProject/lab4/dataset.csv'
    columns = ["user_id", "order_id", "order_time", "order_cost", "success_order_flg"]
    db = sqlite3.connect('')
    cur = db.cursor()
    orders = pd.read_csv(path, encoding='ISO-8859-1', delimiter=';')
    orders['order_time'] = pd.to_datetime(orders['order_time'], unit='s', errors='coerce')
    orders['order_cost'] = pd.to_numeric(orders['order_cost'], errors='coerce')
    orders.dropna()
    orders.to_sql('orders', db, index=False)
    table = cur.execute("SELECT * FROM orders LIMIT 6").fetchall()
    df = pd.DataFrame(table, columns=columns).style.hide(axis='index')
    print(df.to_string())

    cur.executescript(open("views.sql").read())
    table = cur.execute(f'SELECT * FROM Result')
    df = pd.DataFrame(table, columns=['date', 'new sum', 'renew sum', 'sum', 'new count', 'renew count', 'count'])
    print(df.tail(10).style.hide(axis='index').to_string())

    plot = go.Figure(data=[go.Bar(
        name='Новые',
        x=df['date'],
        y=df['new sum']
    ),
        go.Bar(
            name='Реактивированные',
            x=df['date'],
            y=df['renew sum']
        )
    ])
    plot.update_layout(barmode='stack', title='Сумма')
    plot.show()
    #
    plot = go.Figure(data=[go.Bar(
        name='Новые',
        x=df['date'],
        y=df['new count']
    ),
        go.Bar(
            name='Реактивированные',
            x=df['date'],
            y=df['renew count']
        )
    ])
    plot.update_layout(barmode='stack', title='Количество')
    plot.show()