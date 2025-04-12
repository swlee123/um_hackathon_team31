# ⚙️ Configuration Guide

This framework is controlled using a centralized YAML configuration file. Below is a breakdown of each section and its parameters.

---

## 🔧 Basic Settings

| Key | Description |
|-----|-------------|
| `strategy_name` | Name of the backtest run or strategy version. |
| `explaination` | Short description of the strategy and its purpose. |
| `coin_pair` | The crypto trading pair used (e.g., `BTCUSDT`). |
| `mode` | Strategy mode selection. Available options: `rule_based`, `hmm`, `hmm_nlp`. |
| `timeframe` | Candle interval used for strategy (`1m`, `5m`, `15m`, `30m`, `1h`). |

---


## 💰 Portfolio Settings

| Key | Description |
|-----|-------------|
| `initial_capital` | Starting capital in USD for the backtest. |
| `trading_fee` | Fee percentage per trade (e.g., `0.06` = 0.06%). |
| `minimum_trade_frequency` | Strategy must trade at least this percent of the time (e.g., 0.03 = 3%). |

---

## 📁 Data Paths

| Key | Description |
|-----|-------------|
| `data_source_path` | File path to historical OHLCV data in CSV format. |
| `sentiment_data_path` | File path to sentiment data used in `hmm_nlp` mode. |

---



### 📊 Plot

| Key | Description |
|-----|-------------|
| `plot.show_equity_curve` | Show capital over time. |
| `plot.show_profit_loss` | Plot profit/loss per trade. |
| `plot.show_volume` | Display volume bar on price chart. |
| `plot.show_trades` | Mark trade entry/exit on chart. |

### ⚙️ Assumptions

| Key | Description |
|-----|-------------|
| `assumptions.slippage` | Simulated slippage percentage. |
| `assumptions.order_always_filled` | Assume all orders are filled instantly. |
| `assumptions.always_market_order` | Force trade execution at next bar’s open. |
| `assumptions.execution_price` | Use `"open"`, `"close"`, `"high"`, or `"low"` price for execution. |

### 💰 Quantity Configuration

| Key | Description |
|-----|-------------|
| `quantity_config.mode` | `"percentage"` of capital or `"fixed"` amount. |
| `quantity_config.percentage` | Percentage of capital per trade (e.g., 0.05 = 5%). |
| `quantity_config.fixed_quantity` | Fixed dollar amount per trade. |
