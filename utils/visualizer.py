import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_signalsSMA(data):
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

    

    def plotsignalsVWM(data):
        """
        Plots executed trades, RSI values, and volume indicator.

        Parameters:
            data (DataFrame): The backtested data with 'close', 'RSI', 'position', and 'volume'.
        """
        # Identify executed trades
        executed_buy = (data['position'] == 1) & (data['position'].shift() == 0)  # Entered position
        executed_sell = (data['position'] == 0) & (data['position'].shift() == 1)  # Exited position

        fig, axes = plt.subplots(3, 1, figsize=(14, 12), gridspec_kw={'height_ratios': [3, 1, 1]})

        # Price Chart with Executed Trades
        ax1 = axes[0]
        ax1.plot(data.index, data['close'], label='Close Price', color='blue', alpha=0.7)
        ax1.scatter(data.index[executed_buy], data['close'][executed_buy],
                    marker='^', color='green', label='Executed Buy', s=100, alpha=1)
        ax1.scatter(data.index[executed_sell], data['close'][executed_sell],
                    marker='v', color='red', label='Executed Sell', s=100, alpha=1)
        ax1.plot(data.index, data['20_ema'], label='20 EMA', color='orange', linestyle='--', alpha=0.7)
        ax1.set_title('Price with Executed Trades and 20 EMA', fontsize=14)
        ax1.set_ylabel('Price')
        ax1.legend()
        ax1.grid(alpha=0.3)

        # RSI Chart
        ax2 = axes[1]
        ax2.plot(data.index, data['RSI'], label='RSI', color='purple', alpha=0.7)
        ax2.axhline(70, linestyle='--', color='red', label='Overbought (70)')
        ax2.axhline(30, linestyle='--', color='green', label='Oversold (30)')
        ax2.set_title('Relative Strength Index (RSI)', fontsize=14)
        ax2.set_ylabel('RSI Value')
        ax2.legend()
        ax2.grid(alpha=0.3)

        # Volume Chart
        ax3 = axes[2]
        ax3.bar(data.index, data['volume'], label='Volume', color='gray', alpha=0.7)
        ax3.plot(data.index, data['volume_ma'], label='Volume Moving Average (10)', color='orange', linestyle='--', alpha=0.7)
        ax3.set_title('Volume with Moving Average', fontsize=14)
        ax3.set_ylabel('Volume')
        ax3.legend()
        ax3.grid(alpha=0.3)

        plt.tight_layout()
        plt.show()
