from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline



# Data Ingestion Stage
STAGE_NAME = "Data Ingestion Stage"
try:
	logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
	data_ingestion = DataIngestionTrainingPipeline()
	data_ingestion.initate_data_ingestion()
	logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
	logger.exception(e)
	raise e

# Data Validation Stage
STAGE_NAME = "Data Validation Stage"
try:
	logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
	data_validation = DataValidationTrainingPipeline()
	data_validation.initiate_data_validation()
	logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
	logger.exception(e)
	raise e

# Data Transformation Stage
STAGE_NAME = "Data Transformation Stage"
try:
	logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
	data_transformation = DataTransformationPipeline()
	data_transformation.initiate_data_transformation()
	logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
	logger.exception(e)
	raise e

# Model Training Stage
STAGE_NAME = "Model Trainer Stage"
try:
	logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
	model_trainer = ModelTrainerPipeline()
	model_trainer.initiate_model_training()
	logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
	logger.exception(e)
	raise e