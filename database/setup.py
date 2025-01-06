import mysql.connector
import pandas as pd

class DatabaseSetup:
    def __init__(self, host, user, password, database, file_path):
        self.config = {
            'host': host,
            'user': user,
            'password': password
        }
        self.database = database
        self.file_path = file_path
        self.connection = None
        self.cursor = None

    def connect(self):
        """Connect to the MySQL server."""
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor()
        print("Connected to MySQL Server.")

    def create_database(self):
        """Create a new database if it doesn't exist."""
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
        self.cursor.execute(f"USE {self.database}")
        print(f"Database `{self.database}` is ready.")

    def create_table(self):
        """Create the `hindalco` table."""
        table_creation_query = """
        CREATE TABLE IF NOT EXISTS hindalco (
            datetime DATETIME,
            close DECIMAL(10, 2),
            high DECIMAL(10, 2),
            low DECIMAL(10, 2),
            open DECIMAL(10, 2),
            volume BIGINT,
            instrument VARCHAR(256)
        );
        """
        self.cursor.execute(table_creation_query)
        print("Table `hindalco` is ready.")

    def insert_data_from_csv(self):
        # Clear the table first
        self.cursor.execute("DELETE FROM hindalco")
        print("Cleared existing data from the `hindalco` table.")
        """Insert data from the CSV file into the `hindalco` table."""
        data = pd.read_csv(self.file_path)
        for _, row in data.iterrows():
            insert_query = """
            INSERT INTO hindalco (datetime, close, high, low, open, volume, instrument)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            values = (
                row['datetime'], row['close'], row['high'],
                row['low'], row['open'], row['volume'], row['instrument']
            )
            self.cursor.execute(insert_query, values)

        self.connection.commit()
        print(f"{self.cursor.rowcount} rows inserted.")

    def close_connection(self):
        """Close the connection to the database."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection to MySQL Server closed.")
