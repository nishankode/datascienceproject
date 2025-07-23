from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_tranformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_tranformation_config)
        data_transformation.train_test_split()