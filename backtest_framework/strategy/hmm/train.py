import pandas as pd
from hmmlearn.vhmm import VariationalGaussianHMM
from sklearn.preprocessing import StandardScaler
import pickle
import yaml

# === 1. Load Configuration (config.yaml) ===
with open("config/mvp_config.yaml", 'r') as file:
    config = yaml.safe_load(file)

# === 2. Load Dataset ===
df = pd.read_csv(config["data_source_path"], parse_dates=["timestamp"])

# === 3. Preprocess Data ===
features = [
    "close", "volume", "funding_rate", "mvrv", "sopr",
    "stablecoin_supply", "miner_hash_rate", "miner_total_revenue"
]

# hardcoded for now
X = df[features].dropna()

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === 4. Train the HMM Model ===
n_states = 3  

# Number of hidden states
# now we assume as 0,1,2 for bull bear and sideways market 
# hardcoded

model = VariationalGaussianHMM(n_components=n_states, covariance_type="full", n_iter=100)
model.fit(X_scaled)

# === 5. Save the Trained Model into ===

model_saved_path = "um_hackathon_team31\\backtest_framework\\models\\hmm\\model.pkl"
# hard-coded path for now

with open(model_saved_path, 'wb') as f:
    pickle.dump((model, scaler), f)

print(f"Model trained and saved at {model_saved_path}")