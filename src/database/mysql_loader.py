import pandas as pd
from .connection import get_connection

class MySQLLoader:
    def load(self, csv_path: str):
        df = pd.read_csv(csv_path)
        conn = get_connection()
        print(f"Loaded {len(df)} rows from {csv_path}")
        print("Connection established. (Insertion implemented in Sprint 3C)")
        conn.close()
