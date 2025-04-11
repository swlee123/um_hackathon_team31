from datetime import datetime
import pandas as pd
from tqdm import tqdm

# class that act as central engine to run the backtest, driving the strategy and managing the portfolio


class Engine:
    def __init__(self, strategy, data_loader, portfolio, quantity_config,trading_fees,execution_price,logger,evaluator=None):
        self.strategy = strategy  # Strategy object that generates signals
        self.data_loader = data_loader  # DataLoader that provides historical data
        self.portfolio = portfolio  # Portfolio object to manage trades and capital
        self.evaluator = evaluator  # Optional: Used to evaluate performance metrics
        self.current_time = None  # Current timestamp in the simulation
        self.quantity_config = quantity_config  # Configuration for order quantity calculation`
        self.trading_fees = trading_fees  # Trading fees configuration
        self.execution_price = execution_price  # Execution price configuration "open" or "close" or "high" or "low"
        self.logger = logger

    def run(self):
        """
        Run the backtest: iterate through the historical data and simulate the strategy's actions.
        """
        data = self.data_loader.get_data()  # Get historical data
        data = self.strategy.process_data(data)  # Process data with the strategy
        
        
        for timestamp, row in tqdm(data.iterrows(), total=len(data), desc="Backtesting Progress"):
            self.current_time = timestamp  # Set the current time for this iteration

            # Generate trading signal using the strategy
            signal = self.strategy.generate_signal(row)
            
            # Execute the signal: this will either be a buy, sell, or hold
            self.execute_signal(signal, row, self.current_time)
            
            if self.logger:
            # Log the current equity value after executing the signal
                self.logger.log_equity(self.portfolio.current_equity_value, timestamp)
        
            # Evaluate strategy performance (optional)
            if self.evaluator:
                self.evaluator.evaluate(self.portfolio)
        
        # # After the loop ends, we save the history position history equity value and trade log to crosscheck
        
        df = pd.DataFrame(self.portfolio.history_equity_value)
        df.to_csv("Portfolio_his_eq_val.csv")
        print("Saved to Portfolio_his_eq_val.csv for crosscheck")

        # Double Check the cash and btc value in portfolio
        
        print("Cash in Portfolio : ",self.portfolio.cash)
        last_btc_price = data[self.execution_price].iloc[-1]
        
        print(f"BTC position : {self.portfolio.current_positions} BTC last open price : {last_btc_price}")
        value = self.portfolio.current_positions["BTC"] * last_btc_price
        print("BTC total value : ",value)
        print("Total equity (cash + btc) value in usdt :",value+self.portfolio.cash)
        
        # save log to certain directory
        print("Saving log to directory",self.logger.log_dir)

    def execute_signal(self, signal, data_row ,timestamp):
        """
        Execute a trading signal (buy/sell/hold) at the current price.
        """
        if signal == 'buy':
            # Execute a market buy order
            quantity = self.calculate_order_quantity(data_row)
            self.portfolio.buy('BTC', quantity, data_row[self.execution_price],self.trading_fees)
            
            if self.logger:
                self.logger.log_signal(signal,timestamp,data_row[self.execution_price])
                self.logger.log_trade("BUY", quantity, data_row[self.execution_price], timestamp)
                
        elif signal == 'sell':
            # Execute a market sell order
            quantity = self.calculate_order_quantity(data_row)
            self.portfolio.sell('BTC', quantity, data_row[self.execution_price],self.trading_fees)
            
            if self.logger:
                self.logger.log_signal(signal,timestamp,data_row[self.execution_price])
                self.logger.log_trade("SELL", quantity, data_row[self.execution_price], timestamp)
                
                
        elif signal == 'hold':
            # No action needed, hold the position
            self.portfolio.hold('BTC', 0)
        else:
            raise ValueError(f"Invalid signal: {signal}")
        


    def calculate_order_quantity(self, data_row):
        """
        Calculate the quantity of the asset to buy/sell based on the strategy logic.
        There is 2 mode "percentage" and "fixed" for now 
        """
        
        mode = self.quantity_config["mode"]
        if mode == "percentage":
            # Calculate quantity based on a percentage of the portfolio's equity
            percentage = self.quantity_config["percentage"]
            quantity = (self.portfolio.cash * percentage) / data_row[self.execution_price]
            
            # print(f"Cash available : {self.portfolio.cash} Calculated quantity: {quantity} for mode: {mode} with percentage: {percentage} of execution price: {data_row[self.execution_price]}")
            
        elif mode == "fixed":
            # Use a fixed quantity for trading, in usdt
            # Assuming fixed quantity is in USDT
            quantity = self.quantity_config["fixed_quantity"] / data_row[self.execution_price]
        else:
            raise ValueError(f"Invalid quantity mode: {mode}")
        
        # print(f"Calculated quantity: {quantity} for mode: {mode}")
        return quantity
        
