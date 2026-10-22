import joblib
from pathlib import Path

class ModelSerializer:
    def save(self, model, path="models/best_model.joblib"):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, path)

    def load(self, path="models/best_model.joblib"):
        return joblib.load(path)
