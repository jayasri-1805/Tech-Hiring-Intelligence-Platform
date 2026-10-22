"""
Feature Selection Module
"""

from typing import List, Tuple

import pandas as pd


class FeatureSelector:

    TARGET = "salary_midpoint"

    DROP_COLUMNS = [
        "job_id",

        # Target
        "salary_midpoint",

        # Prevent Data Leakage
        "salary_min_usd",
        "salary_max_usd",
        "salary_range",
        "salary_band",
        "high_paying_job",
    ]

    def get_dataset(
        self,
        dataframe: pd.DataFrame,
    ) -> Tuple[pd.DataFrame, pd.Series]:

        X = dataframe.drop(columns=self.DROP_COLUMNS)

        y = dataframe[self.TARGET]

        return X, y

    def numeric_columns(
        self,
        X: pd.DataFrame,
    ) -> List[str]:

        return X.select_dtypes(
            include=[
                "int64",
                "float64",
            ]
        ).columns.tolist()

    def categorical_columns(
        self,
        X: pd.DataFrame,
    ) -> List[str]:

        return X.select_dtypes(
            include=[
                "object",
                "bool",
            ]
        ).columns.tolist()