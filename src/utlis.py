import logging 
import os
from detatime import datetime



LOG_DIR =f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_logs"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


Log_FILE=os.path.join(logs_path,"logs.log")

logging.basicConfig(
    filename=Log_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,


)