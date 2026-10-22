import pandas as pd

class FeatureSelector:

    def correlation_matrix(self, df: pd.DataFrame):
        return df.select_dtypes(include="number").corr()

    def highly_correlated_pairs(self, df: pd.DataFrame, threshold: float = 0.8):
        corr = self.correlation_matrix(df).abs()
        pairs = []
        cols = corr.columns
        for i in range(len(cols)):
            for j in range(i + 1, len(cols)):
                if corr.iloc[i, j] >= threshold:
                    pairs.append((cols[i], cols[j], float(corr.iloc[i, j])))
        return pairs
