import cv2
import logging
import logging
from logger import Logger

class BrightnessAnalyser:
    
    def process_image(self, image):
        # Cover the upper half of the image with black color
        height, width = image.shape[:2]
        image[:height // 2, :, :] = 0  # Set upper half to black
        # Convert the lower half of the image to grayscale
        gray_lower_half = cv2.cvtColor(image[height // 2 :, :], cv2.COLOR_BGR2GRAY)
        # Find the brightest point in the lower half of the image
        _, max_val, _, max_loc = cv2.minMaxLoc(gray_lower_half)
        # Get the width of the lower half of the image
        lower_half_width = width // 2
        # Determine whether the brightest spot is in the lower-left or lower-right quarter
        is_lower_left = max_loc[0] < lower_half_width
        logging.debug("Brightness: %f", max_val)
        logging.debug("Is in lower-left quarter: %r", is_lower_left)

        if logging.debug:
            # Draw on the original image for debugging
            cv2.circle(image, (max_loc[0], max_loc[1] + height // 2), 10, (0, 0, 255), 2)
            cv2.line(image, (lower_half_width, 0), (lower_half_width, height), (255, 0, 0), 2)

        # Return the modified image for logging
        return is_lower_left, image

