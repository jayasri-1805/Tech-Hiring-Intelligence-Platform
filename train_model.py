"""
===========================================================
Tech Hiring Intelligence Platform (THIP)

Machine Learning Training Pipeline

Author : Jaya Sri Patnala
===========================================================
"""

from pathlib import Path
import json
import warnings

import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

# ===========================================================
# THIP Modules
# ===========================================================

from src.ml.feature_selector import FeatureSelector
from src.ml.model_factory import ModelFactory
from src.ml.preprocessing import build_preprocessor
from src.ml.dataset_split import DatasetSplitter
from src.ml.model_serializer import ModelSerializer

warnings.filterwarnings("ignore")


# ===========================================================
# Configuration
# ===========================================================

DATASET_PATH = Path(
    "data/analytics/analytics_dataset.csv"
)

MODEL_DIRECTORY = Path("models")

REPORT_DIRECTORY = Path("reports")

MODEL_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True,
)

REPORT_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True,
)


# ===========================================================
# Training Pipeline
# ===========================================================

class TrainingPipeline:

    def __init__(self):

        self.selector = FeatureSelector()

        self.factory = ModelFactory()

        self.splitter = DatasetSplitter()

        self.serializer = ModelSerializer()

    # -------------------------------------------------------

    def load_dataset(self):

        print("=" * 70)
        print("Loading Dataset...")
        print("=" * 70)

        dataframe = pd.read_csv(DATASET_PATH)

        print(f"Rows    : {dataframe.shape[0]}")
        print(f"Columns : {dataframe.shape[1]}")

        return dataframe

    # -------------------------------------------------------

    def prepare_dataset(self, dataframe):

        print("\nPreparing Features...")

        X, y = self.selector.get_dataset(
            dataframe
        )

        numeric_features = self.selector.numeric_columns(X)

        categorical_features = (
            self.selector.categorical_columns(X)
        )

        print(
            f"Numeric Features     : {len(numeric_features)}"
        )

        print(
            f"Categorical Features : {len(categorical_features)}"
        )

        return (
            X,
            y,
            numeric_features,
            categorical_features,
        )

    # -------------------------------------------------------

    def split_dataset(
        self,
        X,
        y,
    ):

        print("\nSplitting Dataset...")

        return self.splitter.split(
            X,
            y,
            test_size=0.20,
            random_state=42,
        )

    # -------------------------------------------------------

    def build_pipeline(
        self,
        model,
        numeric_features,
        categorical_features,
    ):

        preprocessor = build_preprocessor(
            numeric_features,
            categorical_features,
        )

        pipeline = Pipeline(
            [
                (
                    "preprocessor",
                    preprocessor,
                ),
                (
                    "model",
                    model,
                ),
            ]
        )

        return pipeline
        # -------------------------------------------------------
    # Train Models
    # -------------------------------------------------------

    def train_models(
        self,
        X_train,
        X_test,
        y_train,
        y_test,
        numeric_features,
        categorical_features,
    ):

        print("\n" + "=" * 70)
        print("TRAINING MODELS")
        print("=" * 70)

        trained_models = {}

        model_results = {}

        best_model = None

        best_model_name = None

        best_r2 = float("-inf")

        models = self.factory.get_models()

        for model_name, model in models.items():

            print(f"\nTraining : {model_name}")

            pipeline = self.build_pipeline(
                model,
                numeric_features,
                categorical_features,
            )

            pipeline.fit(
                X_train,
                y_train,
            )

            predictions = pipeline.predict(
                X_test,
            )

            mae = mean_absolute_error(
                y_test,
                predictions,
            )

            rmse = (
                mean_squared_error(
                    y_test,
                    predictions,
                )
                ** 0.5
            )

            r2 = r2_score(
                y_test,
                predictions,
            )

            model_results[model_name] = {

                "MAE": round(mae, 2),

                "RMSE": round(rmse, 2),

                "R2": round(r2, 4),
            }

            trained_models[model_name] = pipeline

            print(
                f"MAE  : {mae:.2f}"
            )

            print(
                f"RMSE : {rmse:.2f}"
            )

            print(
                f"R²   : {r2:.4f}"
            )

            if r2 > best_r2:

                best_r2 = r2

                best_model = pipeline

                best_model_name = model_name

        print("\n" + "=" * 70)
        print("BEST MODEL")
        print("=" * 70)

        print(
            f"Model : {best_model_name}"
        )

        print(
            f"R²    : {best_r2:.4f}"
        )

        return (

            best_model,

            best_model_name,

            model_results,
        )

    # -------------------------------------------------------
    # Save Model
    # -------------------------------------------------------

    def save_model(
        self,
        model,
    ):

        model_path = (
            MODEL_DIRECTORY /
            "best_model.joblib"
        )

        self.serializer.save(
            model,
            model_path,
        )

        print(
            f"\nModel Saved : {model_path}"
        )

        return model_path

    # -------------------------------------------------------
    # Save Report
    # -------------------------------------------------------

    def save_report(
        self,
        model_name,
        results,
    ):

        report = {

            "best_model": model_name,

            "results": results,

        }

        report_path = (
            REPORT_DIRECTORY /
            "model_results.json"
        )

        with open(
            report_path,
            "w",
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
            )

        print(
            f"Report Saved : {report_path}"
        )

        return report_path
        # -------------------------------------------------------
    # Execute Complete Pipeline
    # -------------------------------------------------------

    def run(self):

        # -------------------------------------------
        # Load Dataset
        # -------------------------------------------

        dataframe = self.load_dataset()

        # -------------------------------------------
        # Feature Selection
        # -------------------------------------------

        (
            X,
            y,
            numeric_features,
            categorical_features,
        ) = self.prepare_dataset(
            dataframe
        )

        # -------------------------------------------
        # Dataset Split
        # -------------------------------------------

        (
            X_train,
            X_test,
            y_train,
            y_test,
        ) = self.split_dataset(
            X,
            y,
        )

        print("\nTraining Samples :", len(X_train))
        print("Testing Samples  :", len(X_test))

        # -------------------------------------------
        # Model Training
        # -------------------------------------------

        (
            best_model,
            best_model_name,
            results,
        ) = self.train_models(
            X_train,
            X_test,
            y_train,
            y_test,
            numeric_features,
            categorical_features,
        )

        # -------------------------------------------
        # Save Best Model
        # -------------------------------------------

        self.save_model(
            best_model,
        )

        # -------------------------------------------
        # Save Report
        # -------------------------------------------

        self.save_report(
            best_model_name,
            results,
        )

        # -------------------------------------------
        # Display Final Results
        # -------------------------------------------

        print("\n" + "=" * 70)
        print("MODEL COMPARISON")
        print("=" * 70)

        for model_name, metrics in results.items():

            print(f"\n{model_name}")

            print(
                f"MAE  : {metrics['MAE']}"
            )

            print(
                f"RMSE : {metrics['RMSE']}"
            )

            print(
                f"R²   : {metrics['R2']}"
            )

        print("\n" + "=" * 70)
        print("TRAINING COMPLETED SUCCESSFULLY")
        print("=" * 70)

        return {

            "best_model": best_model_name,

            "results": results,

        }
    # ===========================================================
# Main Function
# ===========================================================

def main():

    print("\n")
    print("=" * 80)
    print("TECH HIRING INTELLIGENCE PLATFORM")
    print("MACHINE LEARNING TRAINING PIPELINE")
    print("=" * 80)

    trainer = TrainingPipeline()

    output = trainer.run()

    print("\n")
    print("=" * 80)
    print("TRAINING SUMMARY")
    print("=" * 80)

    print(f"Best Model : {output['best_model']}")

    print("\nMetrics")

    for model_name, metrics in output["results"].items():

        print("\n" + "-" * 60)

        print(model_name)

        print("-" * 60)

        for metric, value in metrics.items():

            print(f"{metric:<10}: {value}")

    print("\n")

    print("=" * 80)
    print("FILES GENERATED")
    print("=" * 80)

    print("✓ models/best_model.joblib")
    print("✓ reports/model_results.json")

    print("\n")

    print("=" * 80)
    print("THIP MODEL TRAINING COMPLETED SUCCESSFULLY")
    print("=" * 80)


# ===========================================================
# Entry Point
# ===========================================================

if __name__ == "__main__":

    main()