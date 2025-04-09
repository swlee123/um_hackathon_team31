import http.client
import json
from dotenv import load_dotenv
import os
import requests
import pandas as pd
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("X_API_KEY")


res = requests.get(
    "https://api.datasource.cybotrade.rs/binance-spot/candle",
    headers={
      "X-API-key": API_KEY
    },
    params={
        "symbol": "BTCUSDT",
        "interval": "1d",
        "start_time": "1546300800000",   # 1st Jan 2019
        "end_time":    "1672531200000", # 1st Jan 20223
    }
)



data = res.content
data = json.loads(data.decode('utf-8'))
# data = data.decode("utf-8")


print("Response : ",data["data"])
print("Length of data: ", len(data["data"]))
print("First 1 record: ", data["data"][0])
print("Status code:", res.status_code)

# convert unix to utc time 
for row in data["data"]:
    timestamp = row['start_time'] / 1000  # convert ms to seconds
    formatted_date = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y')
    # put back to the row
    row['start_time'] = formatted_date
    
    
df = pd.DataFrame(data["data"])

df.to_csv("BTC_binance_19_22.csv", index=False)
