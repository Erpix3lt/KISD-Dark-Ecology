import cv2
import logging
import logging
from logger import Logger

class BrightnessAnalyser:
    
    def process_image(self, image):
        height, width = image.shape[:2]
        #image[:height // 2, :, :] = 0  # Set upper half to black
        gray_lower_half = cv2.cvtColor(image[height // 2 :, :], cv2.COLOR_BGR2GRAY)
        _, max_val, _, max_loc = cv2.minMaxLoc(gray_lower_half)
        lower_half_width = width // 2
        is_lower_left = max_loc[0] < lower_half_width
        logging.debug("Brightness: %f", max_val)
        logging.debug("Is in lower-left quarter: %r", is_lower_left)

        if logging.getLogger().isEnabledFor(logging.DEBUG):
            cv2.circle(image, (max_loc[0], max_loc[1] + height // 2), 10, (0, 0, 255), 2)
            cv2.line(image, (lower_half_width, 0), (lower_half_width, height), (255, 0, 0), 2)

        return is_lower_left, image

