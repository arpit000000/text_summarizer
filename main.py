from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logger_config.config import logger
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e

