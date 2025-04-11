from backtest.base_strategy import BaseStrategy
import pandas as pd 


class MACrossoverStrategy(BaseStrategy):
    
    def __init__(self, short_window=5, long_window=20):
        super().__init__()
        self.short_window = short_window
        self.long_window = long_window
        self.previous_short = None
        self.previous_long = None

    def process_data(self, df):
        df["sma_short"] = df["close"].rolling(window=self.short_window).mean()
        df["sma_long"] = df["close"].rolling(window=self.long_window).mean()
        return df

    # implement the abstract method from BaseStrategy with own strategy
    def generate_signal(self, row):
        curr_short = row["sma_short"]
        curr_long = row["sma_long"]

        if pd.isna(curr_short) or pd.isna(curr_long):
            return "hold"

        signal = "hold"
        if self.previous_short is not None:
            if self.previous_short <= self.previous_long and curr_short > curr_long:
                signal = "buy"
            elif self.previous_short >= self.previous_long and curr_short < curr_long:
                signal = "sell"

        self.previous_short = curr_short
        self.previous_long = curr_long

        return signal
