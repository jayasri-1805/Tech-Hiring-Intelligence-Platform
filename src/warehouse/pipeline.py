from .database import Database
from .logger import logger
from .loaders.company_loader import CompanyLoader
from .loaders.location_loader import LocationLoader
from .loaders.date_loader import DateLoader
from .loaders.experience_loader import ExperienceLoader
from .loaders.remote_loader import RemoteLoader
from .loaders.salary_loader import SalaryLoader
from .loaders.dimension_writer import DimensionWriter
from .loaders.fact_loader import FactLoader

class WarehousePipeline:

    def test_connection(self):
        conn = Database().connect()
        logger.info("Connected to MySQL")
        conn.close()

    def prepare_dimensions(self,dataframe):
        return {
            "company":CompanyLoader().prepare(dataframe),
            "location":LocationLoader().prepare(dataframe),
            "date":DateLoader().prepare(dataframe),
            "experience":ExperienceLoader().prepare(dataframe),
            "remote":RemoteLoader().prepare(dataframe),
            "salary":SalaryLoader().prepare(dataframe),
        }

    def load_dimensions(self,dataframe):
        dims=self.prepare_dimensions(dataframe)
        writer=DimensionWriter()
        mapping={
            "company":"dim_company",
            "location":"dim_location",
            "date":"dim_date",
            "experience":"dim_experience",
            "remote":"dim_remote",
            "salary":"dim_salary",
        }
        for key,df in dims.items():
            writer.insert_dataframe(df,mapping[key])

    def load_fact_table(self,dataframe):
        FactLoader().load(dataframe)
