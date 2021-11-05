import pyodbc
from shared.utils import configuration


# Setting up database connection
def get_connection():
    conn = pyodbc.connect(configuration.connection_url)
    return conn.cursor()
