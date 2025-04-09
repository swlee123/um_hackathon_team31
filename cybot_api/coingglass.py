import http.client
import json
from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()
API_KEY = os.getenv("X_API_KEY")


res = requests.get(
    'https://api.datasource.cybotrade.rs/coinglass/futures/openInterest/ohlc-history?exchange=Binance&symbol=BTCUSDT&interval=1m',
    headers={
      "X-API-Key": API_KEY
    },
    params={
      "start_time": "1740990814113",
    #   "end_time": "1705067200",
      "limit": "10",
    #   "flatten": "true"
    }
)



data = res.content
data = json.loads(data.decode('utf-8'))
# data = data.decode("utf-8")


print("Response : ",data)
print("Status code:", res.status_code)


df = pd.DataFrame(data)

df.to_csv("coin_glass_data.csv", index=False)
