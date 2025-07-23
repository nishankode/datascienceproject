from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
	logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
	data_ingestion = DataIngestionTrainingPipeline()
	data_ingestion.initate_data_ingestion()
	logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
	logger.exception(e)
	raise e

STAGE_NAME = "Data Validation Stage"
try:
	logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
	data_validation = DataValidationTrainingPipeline()
	data_validation.initiate_data_validation()
	logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
	logger.exception(e)
	raise e

STAGE_NAME = "Data Transformation Stage"
try:
	logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
	data_transformation = DataTransformationPipeline()
	data_transformation.initiate_data_transformation()
	logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
	logger.exception(e)
	raise e