import os
import sys
import logging
print("Logger module loaded successfully!")

logging_str = "[%(asctime)s: %(levelname)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "text_summarizer.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    handlers={
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_filepath)
    }
)

logger = logging.getLogger("textSummarizerLogger")