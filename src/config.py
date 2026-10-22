from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parent.parent
RAW_DATA=PROJECT_ROOT/'data'/'raw'
INTERIM_DATA=PROJECT_ROOT/'data'/'interim'
PROCESSED_DATA=PROJECT_ROOT/'data'/'processed'
REPORTS=PROJECT_ROOT/'reports'

for d in (RAW_DATA,INTERIM_DATA,PROCESSED_DATA,REPORTS):
    d.mkdir(parents=True,exist_ok=True)
