import os
from box.exceptions import BoxValueError
import yaml 
from textSummarizer.logger_config.config import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml_config(path_to_yaml:Path) -> ConfigBox:
    """
    Reads a YAML configuration file and returns a ConfigBox."
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded configuration from: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Invalid YAML format: {e}")
        raise ValueError("Yaml FIle is Empty or Invalid")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise e
    
@ensure_annotations
def create_directory(directory_path: list,verbose=True):
    for path in directory_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def get_size(path:Path) -> str:
    """
    Returns the size of a file in human-readable format."
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
