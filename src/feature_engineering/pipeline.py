from .salary_features import SalaryFeatures
from .experience_features import ExperienceFeatures
from .remote_features import RemoteFeatures
from .company_features import CompanyFeatures
from .time_features import TimeFeatures
from .exporter import AnalyticsExporter

class FeaturePipeline:
    def run(self, df):
        df=SalaryFeatures().transform(df)
        df=ExperienceFeatures().transform(df)
        df=RemoteFeatures().transform(df)
        df=CompanyFeatures().transform(df)
        df=TimeFeatures().transform(df)
        AnalyticsExporter().export(df)
        return df
