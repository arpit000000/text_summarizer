import py7zr
import os
from textSummarizer.constants import *
from textSummarizer.utils.common import get_size
from textSummarizer.logger_config.config import logger
import urllib.request as request
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename} with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with py7zr.SevenZipFile(self.config.local_data_file, mode='r') as z:
            z.extractall(path=unzip_path)
            logger.info(f"Extracted 7z file to: {unzip_path}")


            
        