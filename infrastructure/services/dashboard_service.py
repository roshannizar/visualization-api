from core.context import database
from core.queries import dashboard_query

from collections import Counter

cursor = database.get_connection()


def get_sales_dashboard():
    value = []
    cursor.execute(dashboard_query.sales_query)
    for i in cursor:
        value.append(i[0])

    cursor.execute(dashboard_query.product_query)
    for i in cursor:
        value.append(i[0])

    cursor.execute(dashboard_query.out_of_stock_query)
    for i in cursor:
        value.append(i[0])

    cursor.execute(dashboard_query.user_query)
    for i in cursor:
        value.append(i[0])

    return dict(Counter(value))
