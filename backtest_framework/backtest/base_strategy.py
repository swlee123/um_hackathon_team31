from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    def __init__(self,sentiment_data=False):
        self.signal_history = []
    
    @abstractmethod
    def generate_signal(self, data_row):
        """
        Generate a trading signal based on the data row. 
        (This is where the strategy logic will be implemented in strategy.py)
        """
        pass
    
    @abstractmethod
    def process_data(self, data_loader):
        """
        Process data from data loader and generate signals.
        
        """
        pass 
    