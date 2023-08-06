import os
import logging
import sys


logging_string = "[%(asctime)s : %(levelname)s : %(module)s]: %(message)s"

log_dir = "./logs"

log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_string,
    # Where to render the logging string - Terminal or a file
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout),  # Print log @ the Terminal
    ],
)


logger = logging.getLogger("ipynbRenderer")
