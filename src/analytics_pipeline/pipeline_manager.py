import json
from pathlib import Path
from .metadata import MetadataGenerator
from .statistics import DatasetStatistics

class AnalyticsPipeline:
    def run(self, df):
        metadata=MetadataGenerator().generate(df)
        stats=DatasetStatistics().generate(df)
        report={**metadata,**stats}
        out=Path("reports")
        out.mkdir(exist_ok=True)
        with open(out/"analytics_metadata.json","w",encoding="utf-8") as f:
            json.dump(report,f,indent=4)
        print("Analytics metadata exported.")
        return report
