import pandas as pd

class PredictionService:
    def __init__(self, model):
        self.model=model

    def predict(self,payload:dict):
        data=pd.DataFrame([payload])
        return self.model.predict(data).tolist()
