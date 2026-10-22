class ETLValidator:
    def validate(self, dimensions: dict):
        report = {}
        for name, df in dimensions.items():
            report[name] = {
                "rows": len(df),
                "columns": len(df.columns),
                "duplicates": int(df.duplicated().sum())
            }
        return report
