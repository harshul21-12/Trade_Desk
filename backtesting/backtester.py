import numpy as np

class Backtester:
    def __init__(self, strategy):
        self.strategy = strategy

    def backtestSMA(self, data):
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
    
    

    def backtestVWM(self, data):
        data = self.strategy.generate_signals(data)

        # Execute trades
        data['position'] = 0
        data['position'] = np.where(data['buy_signal'], 1, data['position'])
        data['position'] = np.where(data['sell_signal'], 0, data['position'])

        # Calculate daily returns
        data['daily_returns'] = data['close'].pct_change()

        # Strategy returns only when in position
        data['strategy_returns'] = data['daily_returns'] * data['position'].shift()

        # Track trade results
        data['trade_returns'] = data['strategy_returns'] * data['position']
        winning_trades = data.loc[data['trade_returns'] > 0, 'trade_returns'].count()
        total_trades = data['buy_signal'].sum() + data['sell_signal'].sum()

        # Updated metrics
        aggregated_returns = (1 + data['strategy_returns']).prod() - 1
        win_rate = (winning_trades / total_trades) * 100 if total_trades > 0 else 0
        max_drawdown = ((data['strategy_returns'].cumsum().cummax() - data['strategy_returns'].cumsum()).max()) * 100
        best_trade = data['strategy_returns'].max() * 100
        worst_trade = data['strategy_returns'].min() * 100

        metrics = {
            'Aggregated Returns': aggregated_returns * 100,
            'Win Rate': win_rate,
            'Maximum Drawdown': max_drawdown,
            'Best Trade': best_trade,
            'Worst Trade': worst_trade,
            'Number of Trades': total_trades,
            'Winning trades': winning_trades
        }

        return metrics, data
