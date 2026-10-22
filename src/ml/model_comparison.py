import pandas as pd

class ModelComparison:
    def compare(self, results: dict) -> pd.DataFrame:
        df = pd.DataFrame(results).T
        return df.sort_values(df.columns[0], ascending=False)

    def best_model(self, results: dict, metric: str):
        if metric.lower() == "rmse":
            return min(results.items(), key=lambda x: x[1][metric])
        return max(results.items(), key=lambda x: x[1][metric])
