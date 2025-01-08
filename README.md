# Algorithmic Trading with Backtesting Project

![Screenshot (31)](https://github.com/user-attachments/assets/801dd52f-03f7-41bd-b151-659b1aea4e59)
![trade_desk metrics](https://github.com/user-attachments/assets/d6289c30-cff5-48d3-94be-d03380a6b8be)
![VWM result](https://github.com/user-attachments/assets/57b7b06c-4c59-44af-b1c9-cf8a6351b3a1)


This project implements
1.Simple Moving Average (SMA) Crossover Strategy
2. Volume Weighted Momentum (VWM) Strategy
for backtesting financial data. It includes backtesting functionality, signal visualization,unit testing and performance metric calculation.

## Features
- SMA Crossover strategy implementation
- Volume Weighted Momentum (VWM) strategy
- Backtesting and performance metrics calculation
- Signal visualization with executed trades plotted
- Unit testing

## Requirements
Ensure you have Python installed (version 3.8 or higher recommended). Install the required Python packages using the `requirements.txt` file.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshul21-12/Trade_Desk
   cd Trade_Desk

2. Set up a virtual environment (optional but recommended):
      python -m venv venv
  Activate the virtual environment:
On Windows:
  venv\Scripts\activate
On macOS/Linux:
  source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

Usage
Running the Script
1. Place your historical stock data in the correct format (e.g., a CSV file with columns: datetime, close, etc.).
2. Open a terminal and navigate to the project directory.
3. Run the main script
   python main.py

   NOTE: Make sure that in main.py and test_data.py the details are modified for database connection

Expected Output
The script will display backtesting metrics such as:
   Aggregated Returns
   Number of Trades
   Maximum Drawdown
   Win Rate
   A visualization showing SMA/EMA lines,Relative Strength Index(RSI), Volume with moving average, buy/sell signals, and executed trades will be generated.








