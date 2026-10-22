import pandas as pd

class ExperienceFeatures:
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        result=df.copy()
        bins=[-1,0,2,5,8,100]
        labels=["Intern","Junior","Mid","Senior","Lead"]
        result["experience_bucket"]=pd.cut(
            result["min_experience_years"],
            bins=bins,
            labels=labels
        )
        return result
