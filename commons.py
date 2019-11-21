# -*- encoding: utf-8 -*-

import logging
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', level=logging.INFO)
def log(msg,level="info"):
    if level == "info":
        logging.info(msg)
    elif level == "error":
        logging.error(msg)
    elif level == "debug":
        logging.debug(msg)
    elif level == "warn":
        logging.warning(msg)
    elif level == "critical":
        logging.critical(msg)