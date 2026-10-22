"""
Tech Hiring Intelligence Platform (THIP)

Main Application Entry Point
"""

from src.analytics_pipeline.lineage import DataLineage
from src.analytics_pipeline.pipeline_manager import AnalyticsPipeline
from src.analytics_pipeline.run_history import RunHistory
from src.analytics_pipeline.validator import AnalyticsValidator
from src.feature_engineering.feature_report import FeatureReport
from src.feature_engineering.feature_validator import FeatureValidator
from src.feature_engineering.pipeline import FeaturePipeline
from src.ingestion.data_manager import DataManager
from src.kpi_engine.kpi_pipeline import KPIPipeline
from src.preprocessing.cleaner import DataCleaner
from src.profiling.profiler import DataProfiler
from src.utils.logger import logger
from src.validation.report import ValidationReport
from src.warehouse.pipeline import WarehousePipeline


def main() -> None:
    """Execute the complete THIP analytics pipeline."""

    logger.info("=" * 80)
    logger.info("Tech Hiring Intelligence Platform")
    logger.info("=" * 80)

    # ============================================================
    # Load Dataset
    # ============================================================

    logger.info("Loading dataset...")
    dataframe = DataManager().load_raw_dataset("ai_jobs.csv")
    logger.info("Dataset loaded successfully.")

    # ============================================================
    # Validation
    # ============================================================

    logger.info("Running data validation...")
    ValidationReport().run(dataframe)

    # ============================================================
    # Profiling
    # ============================================================

    logger.info("Running data profiling...")
    DataProfiler().run(dataframe)

    # ============================================================
    # Cleaning
    # ============================================================

    logger.info("Cleaning dataset...")
    clean_dataframe = DataCleaner().run(dataframe)

    # ============================================================
    # Feature Engineering
    # ============================================================

    logger.info("Running feature engineering...")

    analytics_dataframe = FeaturePipeline().run(clean_dataframe)

    FeatureValidator().validate(analytics_dataframe)
    FeatureReport().generate(analytics_dataframe)

    logger.info("Feature engineering completed successfully.")

    # ============================================================
    # KPI Engine
    # ============================================================

    logger.info("Calculating KPIs...")

    kpis = KPIPipeline().run(analytics_dataframe)

    print("\n" + "=" * 80)
    print("KPI SUMMARY")
    print("=" * 80)

    for key, value in kpis.items():
        print(f"{key:<30}: {value}")

    # ============================================================
    # Analytics Metadata
    # ============================================================

    logger.info("Generating analytics metadata...")

    metadata = AnalyticsPipeline().run(analytics_dataframe)

    print("\n" + "=" * 80)
    print("ANALYTICS METADATA")
    print("=" * 80)

    for key, value in metadata.items():
        print(f"{key:<30}: {value}")

    # ============================================================
    # Prepare Warehouse Dimensions (Sprint 3C.2)
    # ============================================================

    logger.info("Preparing Warehouse Dimensions...")

    dimensions = WarehousePipeline().prepare_dimensions(
        analytics_dataframe
    )

    for name, df in dimensions.items():
        print("\n")
        print("=" * 60)
        print(name.upper())
        print("=" * 60)
        print(df.head())

    # ============================================================
    # Analytics Validation
    # ============================================================

    logger.info("Running analytics validation...")

    validation = AnalyticsValidator().validate(analytics_dataframe)

    DataLineage().generate()
    RunHistory().log(validation["status"])

    print("\n" + "=" * 80)
    print("ANALYTICS VALIDATION")
    print("=" * 80)

    for key, value in validation.items():
        print(f"{key:<30}: {value}")

    # ============================================================
    # Dataset Preview
    # ============================================================

    print("\n" + "=" * 80)
    print("ANALYTICS DATASET PREVIEW")
    print("=" * 80)

    print(analytics_dataframe.head())

    # ============================================================
    # Engineered Features
    # ============================================================

    feature_columns = [
        "salary_midpoint",
        "salary_range",
        "salary_band",
        "high_paying_job",
        "experience_bucket",
        "remote_category",
        "is_remote",
        "company_size_rank",
        "company_category",
        "job_market_phase",
        "years_since_posted",
        "dataset_version",
    ]

    print("\n" + "=" * 80)
    print("ENGINEERED FEATURES")
    print("=" * 80)

    print(analytics_dataframe[feature_columns].head())

    # ============================================================
    # Dataset Summary
    # ============================================================

    print("\n" + "=" * 80)
    print("DATASET SUMMARY")
    print("=" * 80)

    print(f"Rows       : {analytics_dataframe.shape[0]}")
    print(f"Columns    : {analytics_dataframe.shape[1]}")

    logger.info("=" * 80)
    logger.info("THIP Pipeline executed successfully.")
    logger.info("=" * 80)


if __name__ == "__main__":
    main()