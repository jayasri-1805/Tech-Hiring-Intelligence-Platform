from pathlib import Path
import pandas as pd

class WarehouseExporter:
    def export(self,df:pd.DataFrame,version:str)->Path:
        out=Path("warehouse")/version
        out.mkdir(parents=True,exist_ok=True)
        path=out/"analytics_dataset.csv"
        df.to_csv(path,index=False)
        return path
