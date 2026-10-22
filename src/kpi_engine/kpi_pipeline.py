import json
from pathlib import Path

import numpy as np

from .company_kpis import CompanyKPIs
from .hiring_kpis import HiringKPIs
from .salary_kpis import SalaryKPIs


class KPIPipeline:

    def run(self, df):

        kpis = {}

        kpis.update(SalaryKPIs().calculate(df))
        kpis.update(HiringKPIs().calculate(df))
        kpis.update(CompanyKPIs().calculate(df))

        # Convert NumPy types to native Python types
        for key, value in kpis.items():

            if isinstance(value, np.integer):
                kpis[key] = int(value)

            elif isinstance(value, np.floating):
                kpis[key] = float(value)

            elif isinstance(value, np.bool_):
                kpis[key] = bool(value)

        output_folder = Path("reports")
        output_folder.mkdir(exist_ok=True)

        with open(
            output_folder / "kpi_summary.json",
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(kpis, file, indent=4)

        print("KPI summary exported.")

        return kpis