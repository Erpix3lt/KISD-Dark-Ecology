import cv2
import os
import time
import logging

class FileService:
    @staticmethod
    def save_image(image, folder="results"):
        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"{folder}/image_{timestamp}.jpg"
        cv2.imwrite(filename, image)
        logging.debug(f"Result saved: {filename}")