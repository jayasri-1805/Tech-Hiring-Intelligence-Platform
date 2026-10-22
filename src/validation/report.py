from pathlib import Path
from .schema_validator import SchemaValidator
from .missing_validator import MissingValueValidator
from .duplicate_validator import DuplicateValidator
from .salary_validator import SalaryValidator

class ValidationReport:
    def run(self,df):
        print("="*70)
        print("VALIDATION REPORT")
        print("="*70)

        SchemaValidator().validate(df)

        dup=DuplicateValidator().validate(df)
        print(f"Duplicate rows : {dup}")

        miss=MissingValueValidator().validate(df)
        print("\nMissing Values")
        print(miss)

        invalid=SalaryValidator().validate(df)
        print(f"\nInvalid salary rows : {len(invalid)}")

        Path("reports").mkdir(exist_ok=True)
        miss.to_csv("reports/missing_value_report.csv")
        invalid.to_csv("reports/invalid_salary_rows.csv",index=False)
        print("\nReports exported to reports/")
