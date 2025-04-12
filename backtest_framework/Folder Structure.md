## Instruction 

### Config 
In **config/mvp_crossover.yaml** contains the setting (assumption we need to make) for backtesting

### Data
Stores In **data/**

### Logs
Contain folder : logs/strategy_name_yyyymmdd_hh_mm_ss/
                 |_equity_curve.csv
                 |_signals.csv
                 |_trades.csv

Stores log information produces by strategy during backtesting

### Sentiment 
In **./sentiment/** , will implement sentiment analysis on social media content (X,reddit,4chan...) to analyse user's sentiment

### Strategy 
In **./strategy/** , ma_crossover.py is an example strategy implmented from **BaseStrategy** class

### Evaluation 
Store evaluation results ( not yet implemented )


### How to use the framework ? 
Use main.py , can refer to code inside
Define all classes in **./backtest/**, make sure to define your own strategy using **BaseStrategy** AbstractClass 

*strategy = MACrossoverStrategy* is just a simple example

Run : 

```bash
python main.py
```
