from database.setup import DatabaseSetup
from database.connection import DatabaseConnection
from database.queries import DataFetcher
from analysis.data_processor import DataProcessor
from analysis.strategies import SMACrossoverStrategy
from backtesting.backtester import Backtester
from utils.visualizer import Visualizer

def main():
    # Step 1: Database Initialization
    db_setup = DatabaseSetup(
        host='localhost',
        user='your_username',
        password='your_password',
        database='database_name',
        file_path='data/HINDALCO.csv'
    )

    db_setup.connect()
    db_setup.create_database()
    db_setup.create_table()
    db_setup.insert_data_from_csv()
    db_setup.close_connection()

    # Step 2: Analyze Data
    db = DatabaseConnection(
        host='localhost',
        user='your_username',
        password='your_password',
        database='database_name'
    )
    connection = db.connect()

    # Fetch data from the database
    fetcher = DataFetcher(connection)
    data = fetcher.fetch_all('hindalco')

    # Step 3: Apply SMA Crossover Strategy
    strategy = SMACrossoverStrategy(short_window=50, long_window=100)
    data = strategy.generate_signals(data)

    # Step 4: Backtesting
    backtester = Backtester(strategy)
    metrics, backtested_data = backtester.backtest(data)

    # Print Metrics
    print("Backtesting Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value}")

    # Step 5: Visualize Results
    Visualizer.plot_signals(backtested_data)

    # Close database connection
    db.close()

if __name__ == "__main__":
    main()
