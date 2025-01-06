class Backtester:
    def __init__(self, strategy):
        self.strategy = strategy

    def backtest(self, data):
        """Simulate trades and calculate metrics."""
        data = self.strategy.generate_signals(data)
        data['position'] = data['signal'].shift()  # Enter trade on next day
        data['daily_returns'] = data['close'].pct_change()
        data['strategy_returns'] = data['daily_returns'] * data['position']

        # Performance metrics
        aggregated_returns = (1 + data['strategy_returns']).prod() - 1  # Compounded return
        metrics = {
            'Aggregated Returns': aggregated_returns * 100,
            'Number of Trades': int(data['position'].diff().abs().sum()) ,
            'Maximum Drawdown': ((data['strategy_returns'].cumsum().cummax() - data['strategy_returns'].cumsum()).max()) * 100,
            'Win Rate': ((data['strategy_returns'] > 0).mean()) * 100,
            'Best Trade': (data['strategy_returns'].max()) * 100,
            'Worst Trade': (data['strategy_returns'].min()) * 100,
            
        }
        return metrics, data
