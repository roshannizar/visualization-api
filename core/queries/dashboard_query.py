sales_graph_query = """SELECT o.Date FROM Orders o WHERE o.Date BETWEEN DateAdd(DAY , -20, GETDATE()) AND GETDATE() AND o.RecordState = 0 ORDER BY o.Date"""

sales_query = """SELECT COUNT(*) FROM Orders o WHERE o.Date BETWEEN GETDATE() AND GETDATE() AND o.RecordState = 0"""
product_query = """SELECT COUNT(*) FROM DescriptionLines d WHERE d.RecordState = 0"""
out_of_stock_query = """SELECT COUNT(*) FROM DescriptionLines d WHERE d.RecordState = 0 AND d.Quantity <=0"""
user_query = """SELECT COUNT(*) FROM Users u WHERE u.RecordState = 0"""
