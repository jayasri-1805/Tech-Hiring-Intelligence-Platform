from pathlib import Path
from datetime import datetime

class RunHistory:
    def log(self,status:str):
        Path("logs").mkdir(exist_ok=True)
        with open("logs/pipeline_history.log","a",encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat(timespec='seconds')} | {status}\n")
