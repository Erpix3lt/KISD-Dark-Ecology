import cv2
import os
import time
import logging
from dotenv import load_dotenv

class Logger:
    def __init__(self):
        load_dotenv()
        log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
        logging.basicConfig(level=log_level)
        if log_level == "DEBUG":
            logging.debug("Debug logging enabled")
            logging.warning("All analysed images will be saved to the _images folder inside the web_server folder. This may take up a lot of disk space.")            

    def save_analysed_images_to_web_server(self, image):
        self.save_image(image, folder="../web_server/_images")

    @staticmethod
    def save_image(image, folder="results"):
        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"{folder}/image_{timestamp}.jpg"
        cv2.imwrite(filename, image)
        logging.debug(f"Result saved: {filename}")

