import logging
from datetime import datetime
import os

def setup_logger(log_level=logging.DEBUG, file_prefix="example", log_folder='logs'):
    
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    current_date = datetime.now().strftime("%Y-%m-%d")

    logger = logging.getLogger()
    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    log_file = os.path.join(log_folder, f"{file_prefix}_{current_date}.log")
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    setup_logger()
