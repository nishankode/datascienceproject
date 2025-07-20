# This is used to create the entire project structure.

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'datascience'

list_of_files=[
    ".github/workflows/.gitkeep", # Deployment
    f"src/{project_name}/__init__.py", # Packaging
    f"src/{project_name}/components.py", # Pipelines
    f"src/{project_name}/utils.py", # Generic fncts
    f"src/{project_name}/utils/common.py", # Common functionalities
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", 
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "setup.py",
    "Dockerfile",
    "research/research.ipynb",
    "templates/index.html"
    ]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory {filedir} for the file : {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating Empty File : {file_path}")
    else:
        logging.info(f"{filename} already exist")