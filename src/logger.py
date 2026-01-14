import logging
import os
from datetime import datetime

# project root = parent of src
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
log_file = os.path.join(LOG_DIR, "app.log")

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s", 
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8")
    ]
)

#resuable logger object: 
logger = logging.getLogger(__name__)