import pandas as pd
import talib
import numpy as np

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

    
class VolumeWeightedMomentumStrategy:
    def __init__(self, rsi_period=7, volume_ma_period=10, trend_ema_period=20, rsi_overbought=70, rsi_oversold=30, volume_multiplier=1.25):
        self.rsi_period = rsi_period
        self.volume_ma_period = volume_ma_period
        self.trend_ema_period = trend_ema_period
        self.rsi_overbought = rsi_overbought
        self.rsi_oversold = rsi_oversold
        self.volume_multiplier = volume_multiplier
    
    def generate_signals(self, data):
        # Calculate RSI
        data['RSI'] = talib.RSI(data['close'], timeperiod=self.rsi_period)

        # Calculate Volume Moving Average (10-day)
        data['volume_ma'] = data['volume'].rolling(window=self.volume_ma_period).mean()

        # Calculate the 20-day EMA for trend confirmation
        data['20_ema'] = data['close'].ewm(span=self.trend_ema_period, adjust=False).mean()

        # Buy Signal: RSI crosses above 30 (from oversold), volume > 1.25 times the moving average, price above 20-day EMA
        data['buy_signal'] = (data['RSI'] > self.rsi_oversold) & (data['volume'] > data['volume_ma'] * self.volume_multiplier) & (data['close'] > data['20_ema'])

        # Sell Signal: RSI crosses below 70 (from overbought), volume > 1.25 times the moving average, price below 20-day EMA
        data['sell_signal'] = (data['RSI'] < self.rsi_overbought) & (data['volume'] > data['volume_ma'] * self.volume_multiplier) & (data['close'] < data['20_ema'])

        return data
