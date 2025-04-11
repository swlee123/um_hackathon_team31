import yaml
import pandas as pd
from strategy.ma_crossover import MACrossoverStrategy
from backtest.data_loader import DataLoader
from backtest.portfolio import Portfolio
from backtest.engine import Engine
from backtest.logger import BacktestLogger


# === 1. Load config.yaml ===
with open("config\mvp_crossover.yaml", 'r') as file:
    config = yaml.safe_load(file)

# === 2. Load data ===
data_path = config["data_source_path"]

# === 3. Initialize components ===
data_loader = DataLoader(data_path)
data = data_loader.load()

strategy = MACrossoverStrategy(
    short_window=5,
    long_window=20
)

portfolio = Portfolio(
    initial_capital=config["initial_capital"],
)


    # def __init__(self,initial_capital):
    #     self.initial_capital = initial_capital
    #     self.history_equity_value = [initial_capital]
    #     self.current_equity_value = initial_capital
    #     self.cash = initial_capital  # Cash available for trading

    #     self.realized_pnl = 0  # PnL from closed positions
    #     self.unrealized_pnl = 0  # PnL from open positions
    #     self.current_positions = {}
    #     self.final_value = None 
    #     self.positions_history = {}
    #     self.trade_log = []
    

logger = BacktestLogger(name=config["strategy_name"])
#     def __init__(self, name='BacktestLogger'):

quantity_config = config["quantity_config"]  # Add this to your config.yaml
execution_price = config["assumptions"]["execution_price"]  # Add this to your config.yaml

# === 4. Engine ===
engine = Engine(
    strategy=strategy,
    data_loader=data_loader,
    portfolio=portfolio,
    quantity_config=quantity_config,
    trading_fees=config["trading_fee"],
    execution_price=execution_price,
    logger=logger
)

    # def __init__(self, strategy, data_loader, portfolio, quantity_config,trading_fees,execution_price,logger,evaluator=None):
    #     self.strategy = strategy  # Strategy object that generates signals
    #     self.data_loader = data_loader  # DataLoader that provides historical data
    #     self.portfolio = portfolio  # Portfolio object to manage trades and capital
    #     self.evaluator = evaluator  # Optional: Used to evaluate performance metrics
    #     self.current_time = None  # Current timestamp in the simulation
    #     self.quantity_config = quantity_config  # Configuration for order quantity calculation`
    #     self.trading_fees = trading_fees  # Trading fees configuration
    #     self.execution_price = execution_price  # Execution price configuration "open" or "close" or "high" or "low"
    #     self.logger = logger
        
        
# === 5. Run the backtest ===
engine.run()
