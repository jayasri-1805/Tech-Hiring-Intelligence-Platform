import joblib
from pathlib import Path


class Serializer:

    def save(
        self,
        model,
        path,
    ):

        Path("models").mkdir(
            exist_ok=True
        )

        joblib.dump(
            model,
            path,
        )

        print(f"Saved -> {path}")

    def load(
        self,
        path,
    ):

        return joblib.load(path)