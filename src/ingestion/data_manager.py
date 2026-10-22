from pathlib import Path
from src.config import RAW_DATA
from .csv_loader import CSVLoader

class DataManager:
    def __init__(self):
        self.loader=CSVLoader()

    def load_raw_dataset(self,file_name:str):
        return self.loader.load(RAW_DATA/file_name)
