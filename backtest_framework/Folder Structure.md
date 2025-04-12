## Folder Explanation

### Config 
In **config/mvp_config.yaml** contains the setting (assumption we need to make) for backtesting

### Data
Stores In 
- **data/market**
BTC OHLCV price data from 2019/1/1 - 2022/12/31
- **data/sentiment**
Dataset to implement sentiment analysis on social media content (Tweeter) to analyse user's sentiment on cryptocurrency

Scripts : 
- correlation_analysis.py 
Scripts to do correlation analysis on dataset and do feature extraction
- data_preprocessing.py
Scripts to normalize and standardize data 

### Logs
Contain folder : **logs/strategy_name_yyyymmdd_hh_mm_ss/**
                 |_equity_curve.csv
                 |_signals.csv
                 |_trades.csv

Stores log information produces by strategy during backtesting

### Strategy 

**./strategy/rule_based** 
- **ma_crossover.py** is an example strategy implmented from **BaseStrategy** class
- strategy derived using indicators should be placed in here

**./strategy/hmm** 
- **hmm_strategy.py** defined strategies based on Hidden Markov Models (HMM) for market regime detection and signal generation. 
  
- **train.py** script to run training on HMM 

**./strategy/hmm_nlp** 

- **hmm_nlp_strategy.py** defined strategies based on Hidden Markov Models (HMM) combined with VADER sentiment analysis for market regime detection and signal generation. 
- **train.py** script to run training on HMM_NLP combination

Flow Diagram for [hmm+nlp](strategy\hmm_nlp\image.png)

### Evaluation (not yet implemented)
**.\evaluation** contain scripts to calculate and plot evaluation metrics like MDD , History Equity Value , Trade Signal History, Trade History and more 

### Model weight
Trained model weight will be store **in models/**

### How to use the framework ? 
Use main.py , you could refer to code inside
Define all classes in **./backtest/**, make sure to define your own strategy using **BaseStrategy** AbstractClass 

*strategy = MACrossoverStrategy* is just a simple example

Run : 

```bash
python main.py
```
