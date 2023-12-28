import cv2
import os
import time

class FileService:
    @staticmethod
    def save_image(image, folder="results"):
        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"{folder}/image_{timestamp}.jpg"
        cv2.imwrite(filename, image)
        print(f"Result saved: {filename}")
