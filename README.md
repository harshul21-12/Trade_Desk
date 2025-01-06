# SMA Crossover Backtesting Project

This project implements a Simple Moving Average (SMA) Crossover Strategy for backtesting financial data. It includes backtesting functionality, signal visualization, and performance metric calculation.

## Features
- SMA Crossover strategy implementation
- Backtesting and performance metrics calculation
- Signal visualization with executed trades plotted

## Requirements
Ensure you have Python installed (version 3.8 or higher recommended). Install the required Python packages using the `requirements.txt` file.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshul21-12/SMAstrategy.git
   cd SMAstrategy

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

Expected Output
The script will display backtesting metrics such as:
   Aggregated Returns
   Number of Trades
   Maximum Drawdown
   Win Rate
   A visualization showing SMA lines, buy/sell signals, and executed trades will be generated.


![Screenshot (31)](https://github.com/user-attachments/assets/801dd52f-03f7-41bd-b151-659b1aea4e59)
![Screenshot (32)](https://github.com/user-attachments/assets/f4051eef-c773-4ebe-8d82-647961450e9e)




