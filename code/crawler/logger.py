import cv2
import os
import time
import logging
from dotenv import load_dotenv

class Logger:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Set up logging
        log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
        logging.basicConfig(level=log_level)

        # Delete existing _images folder and create a new one
        self.reset_images_folder()
        self.images_folder = "../web_server/_images"

        if log_level == "DEBUG":
            logging.debug("Debug logging enabled")
            logging.warning("All analysed images will be saved to the _images folder inside the web_server folder. This may take up a lot of disk space.")

    def reset_images_folder(self):
        if os.path.exists(self.images_folder):
            try:
                for file in os.listdir(self.images_folder):
                    file_path = os.path.join(images_folder, file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            os.rmdir(file_path)
                    except Exception as e:
                        logging.error(f"Error deleting {file_path}: {e}")
                os.rmdir(self.images_folder)
            except Exception as e:
                logging.error(f"Error deleting {self.images_folder}: {e}")
            os.makedirs(self.images_folder)

    def save_analysed_images_to_web_server(self, image):
        self.save_image(image, folder=self.images_folder)

    @staticmethod
    def save_image(image, folder="results"):
        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"{folder}/image_{timestamp}.jpg"
        cv2.imwrite(filename, image)
        logging.debug(f"Result saved: {filename}")
