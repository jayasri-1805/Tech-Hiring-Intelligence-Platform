import json
from pathlib import Path

class ManifestGenerator:
    def generate(self,path:str,rows:int,columns:int,version:str)->None:
        manifest={
            "dataset_path":path,
            "rows":rows,
            "columns":columns,
            "version":version
        }
        with open(Path(path).parent/"manifest.json","w",encoding="utf-8") as f:
            json.dump(manifest,f,indent=4)
