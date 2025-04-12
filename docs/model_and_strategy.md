# 📊 Model and Strategy Design

## 🔧 Common Assumptions Across All Strategies

For the sake of building a Minival Viable Product , these are default assumptions for the testing framework.

| Parameter               | Description |
|------------------------|-------------|
| `coin_pair`            | The cryptocurrency pair used for trading (e.g., `BTCUSDT`). |
| `timeframe`            | 30m (30minutes) |
| `initial_capital`      | 100k USDT |
| `trading_fee`          | 0.06 |
| `slippage`             | Set to `0.00` — assumes perfect execution. |
| `order_always_filled`  | Assumes all orders are filled without delay. |
| `execution_price`      | Market `open` price is used as execution price for signal  |
| `quantity_config`      | `percentage` , assume each `buy/sell` is 5% of current cash  |

---

## 1️⃣ Rule-Based Strategy

### Example

This strategy uses predefined technical indicators and logical rules to generate trading signals (`buy`, `sell`, `hold`).

### 📂 Class: `MACrossoverStrategy`

| Component        | Description |
|------------------|-------------|
| **Location**     | `strategy/rule_based/ma_crossover.py` |
| **Inherits**     | `BaseStrategy` |
| **Signal Logic** | Generates signal when short-term MA crosses long-term MA. |

### ⚙️ Example Parameters

- `short_window`: Number of candles for short-term moving average.
- `long_window`: Number of candles for long-term moving average.

### 🧠 Example Signal Logic
```python
if sma_short > sma_long and previous_sma_short <= previous_sma_long:
    return "buy"
elif sma_short < sma_long and previous_sma_short >= previous_sma_long:
    return "sell"
else:
    return "hold"

```

## 2️⃣ HMM Strategy

### ✅ Overview

The **HMM-Based Strategy** leverages a **Hidden Markov Model (HMM)** to identify latent market regimes based on historical data (OHLCV, volume, on-chain data, etc.). These regimes are used to generate probabilistic signals for trading (`buy`, `sell`, or `hold`). This strategy predicts the current market condition and adapts accordingly to detect favorable market regimes for trading.

### 📂 Class: `HMMStrategy`

| Component        | Description |
|------------------|-------------|
| **Location**     | `strategy/hmm/hmm_strategy.py` |
| **Inherits**     | `BaseStrategy` |
| **Signal Logic** | Generates trading signals based on the market regime (state) identified by the HMM. |

### ⚙️ Parameters

- **`n_states`**: Number of hidden states in the HMM (e.g., 3 states: Bullish ,Bearish, Consolidate).
- **`model_path`**: Path to save/load the trained HMM model.

## 3️⃣ HMM + NLP Strategy 

### ✅ Overview (not yet implemented MVP)

The **HMM + NLP Strategy** combines the power of **Hidden Markov Models (HMM)** with **Natural Language Processing (NLP)** to generate trading signals. The strategy first uses the HMM to identify underlying market regimes (such as bullish, bearish, or neutral). Then, it integrates sentiment data derived from NLP techniques (e.g., **[VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)** to provide additional insights into market sentiment. The combination of both market regimes and sentiment analysis leads to more informed trading decisions.

### 📂 Class: `HMMNLPStrategy`

| Component        | Description |
|------------------|-------------|
| **Location**     | `strategy/hmm_nlp/hmm_nlp_strategy.py` |
| **Inherits**     | `HMMStrategy` |
| **Signal Logic** | Generates trading signals based on market regimes (HMM) combined with sentiment scores (NLP). |

### ⚙️ Parameters


- **`n_states`**: Number of hidden states in the HMM (e.g., 3 states: Bullish ,Bearish, Consolidate).
- **`model_path`**: Path to save/load the trained HMM model.


## Summary
Both HMM-Based Strategy and HMM + NLP Strategy rely on the Hidden Markov Model (HMM) for detecting market regimes and making predictions. The key difference is that the HMM + NLP Strategy integrates additional sentiment analysis from tweeter post dataset to provide a more holistic view of market conditions, which can improve decision-making by incorporating social media sentiment data.

The general architecture follows the BaseStrategy class design, where each strategy inherits and overrides the necessary methods to implement the specific logic. This modular design allows for easy switching between strategies for different backtesting and trading scenarios.


For implementation details of each strategy, visit the corresponding Python modules in the `backtest_framework\strategy` directory.