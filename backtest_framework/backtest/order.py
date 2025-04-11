from datetime import datetime 

class Order : 
    
    def __init__(self,symbol,quantity,price,side,timestamp):
        
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.side = side
        self.timestamp = timestamp # YYYY-MM-DD HH:MM:SS format
        self.status = "filled" # Order status can be "filled", "partially_filled", or "canceled" , for poc assume only "filled for all"
    
    def __repr__(self):
        return f"Order(symbol={self.symbol}, quantity={self.quantity}, price={self.price}, side={self.side}, timestamp={self.timestamp}, status={self.status})"