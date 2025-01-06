import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_signals(data):
        # Identify actual trades (position changes)
        data['trade'] = data['position'].diff().abs() > 0

        # Filter buy and sell trades
        buy_trades = data[(data['trade']) & (data['position'] > 0)]  # Position changes to buy
        sell_trades = data[(data['trade']) & (data['position'] < 0)]  # Position changes to sell

        # Create plot
        plt.figure(figsize=(14, 7))
        plt.plot(data['datetime'], data['close'], label='Close Price', color='blue', alpha=0.5)
        plt.plot(data['datetime'], data['SMA_short'], label='Short SMA', linestyle='--', color='orange')
        plt.plot(data['datetime'], data['SMA_long'], label='Long SMA', linestyle='--', color='purple')

        # Plot executed trades
        plt.scatter(buy_trades['datetime'], buy_trades['close'], label='Buy Trade', marker='^', color='green', s=100)
        plt.scatter(sell_trades['datetime'], sell_trades['close'], label='Sell Trade', marker='v', color='red', s=100)

        # Add titles, labels, and legend
        plt.title('SMA Crossover Strategy with Executed Trades')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()
