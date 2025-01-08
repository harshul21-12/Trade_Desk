import unittest
import pandas as pd
from database.setup import DatabaseSetup
from database.connection import DatabaseConnection
from database.queries import DataFetcher

class TestRealDataFetcher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up database and fetch data before running tests."""
        # Step 1: Database Initialization
        db_setup = DatabaseSetup(
            host='localhost',
            user='your_username',
            password='your_password!',
            database='your_database',
            file_path='data/HINDALCO.csv'
        )

        db_setup.connect()
        db_setup.create_database()
        db_setup.create_table()
        db_setup.insert_data_from_csv()
        db_setup.close_connection()

        # Step 2: Database Connection
        cls.db = DatabaseConnection(
            host='localhost',
            user='your_username',
            password='your_password!',
            database='your_database'
        )
        cls.connection = cls.db.connect()

        # Step 3: Fetch data from the database
        fetcher = DataFetcher(cls.connection)
        cls.data = fetcher.fetch_all('hindalco')

    def test_valid_data_structure(self):
        """Test if fetched data has the correct structure and types."""
        data = self.data

        # Ensure data is not empty
        self.assertFalse(data.empty, "Fetched data is empty!")

        # Ensure all required columns are present
        expected_columns = ['datetime', 'open', 'high', 'low', 'close', 'volume', 'instrument']
        self.assertTrue(all(col in data.columns for col in expected_columns), "Missing required columns!")

        # Ensure datetime is correct type
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(data['datetime']), "Datetime column has incorrect type!")

        # Ensure numeric columns are correct type
        for col in ['open', 'high', 'low', 'close']:
            self.assertTrue(pd.api.types.is_float_dtype(data[col]), f"{col} column has incorrect type!")

        # Ensure volume is integer type
        self.assertTrue(pd.api.types.is_integer_dtype(data['volume']), "Volume column has incorrect type!")

        # Ensure instrument is string type
        self.assertTrue(pd.api.types.is_string_dtype(data['instrument']), "Instrument column has incorrect type!")

    def test_data_values(self):
        """Test if data values are within logical bounds."""
        data = self.data

        # Ensure all price columns are positive
        for col in ['open', 'high', 'low', 'close']:
            self.assertTrue((data[col] > 0).all(), f"{col} column contains non-positive values!")

        # Ensure volume is positive
        self.assertTrue((data['volume'] > 0).all(), "Volume column contains non-positive values!")

        # Ensure high >= low
        self.assertTrue((data['high'] >= data['low']).all(), "High is less than low in some rows!")

        # Ensure datetime is unique
        self.assertTrue(data['datetime'].is_unique, "Datetime column contains duplicate values!")

    @classmethod
    def tearDownClass(cls):
        """Close database connection after tests are complete."""
        cls.db.close()

if __name__ == '__main__':
    unittest.main()
