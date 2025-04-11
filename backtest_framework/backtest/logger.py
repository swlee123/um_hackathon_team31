import logging
from datetime import datetime
import os
import csv

class BacktestLogger:
    def __init__(self, name='BacktestLogger'):
        self.log_dir = f"logs/{name}_{datetime.now().strftime('%Y%m%d_%H_%M_%S')}"
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Define log file paths
        self.signal_log = os.path.join(self.log_dir, "signals.csv")
        self.trade_log = os.path.join(self.log_dir, "trades.csv")
        self.equity_log = os.path.join(self.log_dir, "equity_curve.csv")

        # Create CSV files with headers
        self._init_csv(self.signal_log, ["timestamp", "signal", "price"])
        self._init_csv(self.trade_log, ["timestamp", "side", "quantity", "price"])
        self._init_csv(self.equity_log, ["timestamp", "equity_value"])
        
        

    def _init_csv(self, path, headers):
        with open(path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

    def log_signal(self, signal, timestamp, price):
        with open(self.signal_log, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, signal, price])

    def log_trade(self, side, quantity, price, timestamp):
        with open(self.trade_log, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, side, quantity, price])

    def log_equity(self, equity_value, timestamp):
        with open(self.equity_log, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, equity_value])