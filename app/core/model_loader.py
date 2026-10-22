import joblib
from pathlib import Path


class ModelLoader:

    def __init__(
        self,
        model_path="models/best_model.joblib",
    ):

        self.model_path = Path(model_path)

        self.model = None

    def load(self):

        if not self.model_path.exists():

            raise FileNotFoundError(
                f"{self.model_path} not found."
            )

        self.model = joblib.load(
            self.model_path
        )

        return self.model