class DistributionAnalysis:

    def summarize(self, df):
        summary = {}
        for col in df.select_dtypes(include="number").columns:
            summary[col] = {
                "mean": float(df[col].mean()),
                "median": float(df[col].median()),
                "std": float(df[col].std())
            }
        return summary
