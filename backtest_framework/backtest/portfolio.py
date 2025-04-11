class Portfolio:
    def __init__(self,initial_capital):
        self.initial_capital = initial_capital
        self.history_equity_value = [initial_capital]
        self.current_equity_value = initial_capital
        self.cash = initial_capital  # Cash available for trading

        self.realized_pnl = 0  # PnL from closed positions
        self.unrealized_pnl = 0  # PnL from open positions
        self.current_positions = {}
        self.final_value = None 
        self.positions_history = {}
        self.trade_log = []
    
    
    def log_equity_value(self):

        self.history_equity_value.append(self.current_equity_value)

        self.final_value = self.history_equity_value[-1]
    
    def update_equity_value(self, current_price):
        
        self.log_equity_value()  # log the equity value before updating it
        
        # update it every epoch based on current_equity = cash(usdt) + position*price
        # check if current position is empty 
        if not self.current_positions:
            self.current_equity_value = self.cash
        else:
            
            self.current_equity_value = self.cash + sum([self.current_positions["BTC"] * current_price])
        
        
    
    def buy(self, symbol, quantity, price):
        if symbol in self.current_positions:
            self.current_positions[symbol] += quantity
        else:
            self.current_positions[symbol] = quantity

        cost = quantity * price
        self.cash -= cost
        self.update_equity_value(price)  # Update equity value after buying
        
        self.trade_log.append((symbol, quantity, price, 'buy'))
    
    def sell(self, symbol, quantity, price):
        if symbol in self.current_positions:
            if self.current_positions[symbol] >= quantity:
                self.current_positions[symbol] -= quantity
                if self.current_positions[symbol] == 0:
                    del self.current_positions[symbol]
            else:
                print("No enough position to sell ,current position is ",self.current_positions[symbol])
        else:
            print(f"No position for {symbol} to sell")
            return

        revenue = quantity * price
        self.cash += revenue
        self.update_equity_value(price)
        
        self.trade_log.append((symbol, quantity, price, 'sell'))
        
    def hold(self, symbol, quantity):
        # do nothing 
        self.log_equity_value()  # log the equity value without any change
    
        
