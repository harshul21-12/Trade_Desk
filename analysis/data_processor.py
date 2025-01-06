class DataProcessor:
    @staticmethod
    def calculate_moving_averages(data, window):
        data[f'SMA_{window}'] = data['close'].rolling(window=window).mean()
        return data
