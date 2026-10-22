from .pipeline import WarehousePipeline
from .utils.etl_validator import ETLValidator
from .utils.etl_logger import etl_logger

class ETLRunner:

    def run(self, dataframe):
        pipeline = WarehousePipeline()

        etl_logger.info("Preparing dimensions...")
        dims = pipeline.prepare_dimensions(dataframe)

        report = ETLValidator().validate(dims)

        etl_logger.info("Loading dimensions...")
        pipeline.load_dimensions(dataframe)

        etl_logger.info("Loading fact table...")
        pipeline.load_fact_table(dataframe)

        return report
