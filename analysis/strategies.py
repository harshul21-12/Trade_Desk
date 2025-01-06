import pandas as pd

class SMACrossoverStrategy:
    def __init__(self, short_window=50, long_window=100):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data):
        """Generate buy/sell signals based on SMA crossover."""
        data['SMA_short'] = data['close'].rolling(window=self.short_window).mean()
        data['SMA_long'] = data['close'].rolling(window=self.long_window).mean()
        data['signal'] = 0
        data.loc[data['SMA_short'] > data['SMA_long'], 'signal'] = 1  # Buy signal
        data.loc[data['SMA_short'] <= data['SMA_long'], 'signal'] = -1  # Sell signal
        return data

