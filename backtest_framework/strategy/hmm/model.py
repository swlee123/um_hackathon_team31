import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

class HMMModel:
    def __init__(self, model_path):
        # Load the trained model and scaler
        with open(model_path, 'rb') as f:
            self.model, self.scaler = pickle.load(f)

    def predict(self, df, features):
        # Preprocess and scale the input data
        X = df[features].dropna()
        X_scaled = self.scaler.transform(X)

        # Predict the hidden states
        hidden_states = self.model.predict(X_scaled)
        return hidden_states

    def predict_single(self, data_row, features):
        # Predict the state for a single data row
        data_row_scaled = self.scaler.transform([data_row[features]])
        hidden_state = self.model.predict(data_row_scaled)
        return hidden_state[0]