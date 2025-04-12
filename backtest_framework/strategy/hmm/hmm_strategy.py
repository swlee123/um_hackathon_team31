from abc import ABC, abstractmethod
import pandas as pd
from .model import HMMModel
from backtest.base_strategy import BaseStrategy

class HMMStrategy(BaseStrategy):
    def __init__(self, model_path, scaler, n_states=3):
        # Load the trained HMM model and scaler
        self.hmm_model = HMMModel(model_path)
        self.n_states = n_states
        self.signal_history = []

    def process_data(self, data_loader):
        # Load data from data loader
        df = data_loader.load()

        # Get the hidden states from the model
        hidden_states = self.hmm_model.predict(df, features=["close", "volume", "funding_rate", "mvrv", "sopr", 
                                                             "stablecoin_supply", "miner_hash_rate", "miner_total_revenue"])

        # Add the hidden states as a new column
        df["hidden_state"] = hidden_states

        # Generate signals based on hidden states (customizable logic)
        df["signal"] = df["hidden_state"].apply(self.state_to_signal)

        return df

    def state_to_signal(self, state):
        # Map states to buy/sell/hold signals
        if state == 0:
            return "buy"
        elif state == 1:
            return "sell"
        else:
            return "hold"

    def generate_signal(self, data_row):
        # Generate a signal based on the state of the row
        return data_row["signal"]