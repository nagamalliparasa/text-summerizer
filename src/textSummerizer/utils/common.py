import os

from box.exceptions import BoxValueError
import yaml
from textSummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    reads yaml file and returns 

    args: path_to_yaml

    raises:
        ValueError: if yaml file is empty 

    returns: 
        ConfigBox: ConfigBox type

    """

    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("Yaml file Empty")
    
    except Exception as e: 
        raise e
    


@ensure_annotations 
def create_directories(path_to_directories:list,verbose=True):
    """Create a list of directories"""

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

        
@ensure_annotations
def get_size(path:Path)->str:
    """
    get size in kB"""
    
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"