import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load(self):
        self.data = pd.read_csv(self.filepath, parse_dates=['timestamp'])
        self.data.set_index('timestamp', inplace=True)
        return self.data

    def get_data(self):
        if self.data is None:
            return self.load()
        return self.data
