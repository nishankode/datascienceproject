# Common functionalities for the project

import os
import yaml 
from src.datascience import logger
import json 
import joblib
from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file to be read.

    Returns:
        ConfigBox: Parsed YAML content wrapped inside a ConfigBox object.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For any other errror during the process.

    """

    try:
        # Open and read the yaml file
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            # Log
            logger.info(f"YAML File: {path_to_yaml} Loaded Successfully.")
            # Return the content of YAML File as ConfigBox
            return ConfigBox(content)
        
    # Exception Handling
    except BoxValueError:
        # If file is empty
        raise ValueError("YAML File is Empty")
    
    except Exception as e:
        # For any other errors during process
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create a list of directories from the input list.

    Args:
        path_to_directories (list): List of path of directories.
        verbose (bool, optional): Condition to whether log the dir creation. default True.
    """

    # For ech path, creating directory
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        # Logging if verbose True
        if verbose:
            logger.info(f"Created Directory at {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data to JSON file.

    Args:
        path (Path): Path to the json file to be saved.
        data (dict): Data to be saved to json file.
    """

    # Saving the data to JSON file
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    # Logging
    logger.log(f"JSON file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON files data.

    Args:
        path (Path): path to JSON file.

    Returns:
        ConfigBox: JSON Data wrapped inside a ConfigBox.

    """

    # Reading the data from json file
    with open(path, 'r') as f:
        content = json.load(f)

    # Logging
    logger.info(f"JSON file loaded successfuly from: {path}")

    # Returning
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save Binary Files

    Args:
        data (Any): Data to be saved as Binary.
        path (Path): Path where the binary is to be saved.
    """

    # Saving data to binary
    joblib.dump(value=data, filename=path)
    # Logging
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load Binary Files

    Args:
        path (Path): Path of the binary file to be read.

    Returns:
        Any: Object stored inside the file (any type).
    """

    # Loading the binary file
    data = joblib.load(path)

    # Logging
    logger.info(f"Binary file loaded from: {path}")

    # Return
    return data