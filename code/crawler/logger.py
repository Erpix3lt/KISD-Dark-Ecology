import cv2
import os
import time
import logging
from dotenv import load_dotenv

class Logger:
    def __init__(self):
        load_dotenv()
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        logging.basicConfig(level=log_level)

    @staticmethod
    def save_image(image, folder="results"):
        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"{folder}/image_{timestamp}.jpg"
        cv2.imwrite(filename, image)
        logging.debug(f"Result saved: {filename}")

