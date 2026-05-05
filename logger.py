import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name, log_file, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear old handlers (important for pytest rerun)
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.propagate = False
    return logger


debug_logger = setup_logger(
    "debug_logger",
    f"{LOG_DIR}/Chargeback_Debug_log.txt",
    logging.DEBUG
)

info_logger = setup_logger(
    "info_logger",
    f"{LOG_DIR}/Chargeback_Info_log.txt",
    logging.INFO
)

error_logger = setup_logger(
    "error_logger",
    f"{LOG_DIR}/Chargeback_Error_log.txt",
    logging.ERROR
)