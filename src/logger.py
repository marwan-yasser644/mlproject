import logging
import os
from datetime import datetime

log_dir = os.path.join(os.getcwd(), "logs", f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_logs")
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, "logs.log")

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)

