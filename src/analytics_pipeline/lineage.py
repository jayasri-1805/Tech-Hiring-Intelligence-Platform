from pathlib import Path

class DataLineage:
    def generate(self):
        Path("reports").mkdir(exist_ok=True)
        with open("reports/data_lineage.txt","w",encoding="utf-8") as f:
            f.write(
"""Raw Dataset
   |
Validation
   |
Profiling
   |
Cleaning
   |
Feature Engineering
   |
KPI Engine
   |
Analytics Metadata
   |
Warehouse Export
""")
