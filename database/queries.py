import pandas as pd

class DataFetcher:
    def __init__(self, connection):
        self.connection = connection

    def fetch_all(self, table_name):
        query = f"SELECT * FROM {table_name}"
        return pd.read_sql(query, self.connection)
