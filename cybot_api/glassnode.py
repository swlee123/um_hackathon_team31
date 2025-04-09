import http.client
import json
from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()
API_KEY = os.getenv("X_API_KEY")


res = requests.get(
    'https://api.datasource.cybotrade.rs/glassnode/blockchain/utxo_created_value_median?a=BTC&c=usd&i=1h',
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


print("Response : ",data)
print("Status code:", res.status_code)


df = pd.DataFrame(data["data"])

df.to_csv("glassnode_data.csv", index=False)
