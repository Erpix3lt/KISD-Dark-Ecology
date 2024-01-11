import cv2
import logging
import logging
from logger import Logger

class BrightnessAnalyser:
    
    def process_image(self, image):
        height, width = image.shape[:2]
        # Set upper half to black
        image[:height // 2, :, :] = 0  
        # Convert to grayscale
        gray_lower_half = cv2.cvtColor(image[height // 2 :, :], cv2.COLOR_BGR2GRAY)
        # Add gausian blur, to prevent noise mistakes
        gray_lower_half = cv2.GaussianBlur(gray_lower_half, (5, 5), 0)
        # Get max brightness value and location
        _, max_val, _, max_loc = cv2.minMaxLoc(gray_lower_half)
        lower_half_width = width // 2
        is_lower_left = max_loc[0] < lower_half_width
        logging.debug("Brightness: %f", max_val)
        logging.debug("Is in lower-left quarter: %r", is_lower_left)

        if logging.getLogger().isEnabledFor(logging.DEBUG):
            cv2.circle(gray_lower_half, (max_loc[0], max_loc[1] + height // 2), 10, (0, 0, 255), 2)
            cv2.line(gray_lower_half, (lower_half_width, 0), (lower_half_width, height), (255, 0, 0), 2)

        return is_lower_left, gray_lower_half

