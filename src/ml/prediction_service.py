class PredictionService:
    def __init__(self, model, preprocessor=None):
        self.model=model
        self.preprocessor=preprocessor

    def predict(self, X):
        if self.preprocessor is not None:
            X=self.preprocessor.transform(X)
        return self.model.predict(X)
