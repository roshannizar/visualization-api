from core.context import database
from core.queries import report_query

cursor = database.get_connection()


# Sales report
def sales_report(from_date, to_date):
    param_tuple = (from_date, to_date)
    return cursor.execute(report_query.sales_report_query, param_tuple)
