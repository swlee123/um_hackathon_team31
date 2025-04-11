class Evaluator():
    def __init__(self, portfolio, logger):
        self.portfolio = portfolio
        self.logger = logger
        
    def evaluate(self):
        # Calculate performance metrics
        total_return = self.portfolio.final_value - self.portfolio.initial_capital
        total_return_percentage = (total_return / self.portfolio.initial_capital) * 100
        
        # Log the results
        self.logger.info(f"Total Return: {total_return} ({total_return_percentage:.2f}%)")
        
        # You can add more metrics here, such as Sharpe ratio, max drawdown, etc.
    def calculate_sharpe_ratio(self, risk_free_rate=0.0):

        # todo 
        pass 
    
    def calculate_max_draw_down(args):
        # todo 
        pass 
    
    def calculate_trading_frequency(args):
        # todo 
        pass
    
    def calculate_win_loss_ratio(args):
        # todo 
        pass