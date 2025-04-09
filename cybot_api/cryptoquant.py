import http.client
import json
from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()
API_KEY = os.getenv("X_API_KEY")


res = requests.get(
    'https://api.datasource.cybotrade.rs/cryptoquant/btc/exchange-flows/inflow?exchange=okx&window=hour',
    headers={
      "X-API-key": API_KEY
    },
    params={
      "start_time": "1577836800000",
    #   "end_time": "1705067200",
      "limit": "10",
    #   "flatten": "true"
    }
)



data = res.content
data = json.loads(data.decode('utf-8'))
# data = data.decode("utf-8")


print("Response : ",data["data"])
print("Status code:", res.status_code)


df = pd.DataFrame(data["data"])

df.to_csv("crypto_quant_data.csv", index=False)
