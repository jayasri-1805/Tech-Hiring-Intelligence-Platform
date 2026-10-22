import pandas as pd

class InferenceEngine:
    def __init__(self, model):
        self.model=model

    def predict(self, data):
        if isinstance(data, dict):
            data=pd.DataFrame([data])
        return self.model.predict(data)
