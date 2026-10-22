import json
from pathlib import Path


class ReportGenerator:

    def save(
        self,
        results,
        path="reports/model_results.json",
    ):

        Path("reports").mkdir(exist_ok=True)

        with open(path, "w") as f:

            json.dump(
                results,
                f,
                indent=4,
            )

        print(f"Report saved -> {path}")