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
        
        
    
    def buy(self, symbol, quantity, price,trading_fees):

        # Calculate cost of trade 
        cost = quantity * price

        # Check if the cost is below the minimum order size (hardcoded)
        if cost < 10:
            # print("Cost : ", cost)
            # print("Lower than minimum order size")
            # print log 
            pass
        # Check if there is enough cash to buy
        elif cost > self.cash:
            # print("Cost", cost)
            # print("Cash", self.cash)
            # print("Not enough cash to buy")
            pass 
            
        # OK BUY
        else :
            if symbol in self.current_positions:
                self.current_positions[symbol] += quantity
            else:
                self.current_positions[symbol] = quantity

            # Deduct trading fees from the cost
            cost += cost * trading_fees  # Assuming trading_fees is a percentage (e.g., 0.001 for 0.1%)
            self.cash -= cost
            self.trade_log.append((symbol, quantity, price, 'buy'))
            
        self.update_equity_value(price)  # Update equity value after buying/not buying 
        
    
    
    def sell(self, symbol, quantity, price,trading_fees):
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
        # Deduct trading fees from the revenue
        revenue -= revenue * trading_fees
        # Add the revenue to cash
        self.cash += revenue
        self.update_equity_value(price)
        
        self.trade_log.append((symbol, quantity, price, 'sell'))
        
    def hold(self, symbol, quantity):
        # do nothing 
        self.log_equity_value()  # log the equity value without any change
    
        
