import cv2
import logging

class BrightnessAnalyser:

    def process_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
        width = image.shape[1]
        is_left = max_loc[0] < width / 2
        logging.debug("Brightness: %f", max_val)
        return is_left
