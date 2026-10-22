from pathlib import Path
import pandas as pd
from .file_manager import FileManager

class CSVLoader:
    def load(self,path:Path)->pd.DataFrame:
        FileManager.validate_csv(path)
        return pd.read_csv(path)
