from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
if __name__ == '__main__':
	try:
		logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
		data_ingestion = DataIngestionTrainingPipeline()
		data_ingestion.initate_data_ingestion()
		logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")
	except Exception as e:
		logger.exception(e)
		raise e