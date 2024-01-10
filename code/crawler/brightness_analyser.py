import cv2
import logging
import os


class BrightnessAnalyser:

    def process_image(self, image):
        # Cover the upper half of the image with black color
        height, width = image.shape[:2]
        image[:height // 2, :, :] = 0  # Set upper half to black

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Find the brightest point in the lower half of the image
        _, max_val, _, max_loc = cv2.minMaxLoc(gray[height // 2 :, :])

        # Get the width of the lower half of the image
        lower_half_width = width // 2

        # Determine whether the brightest spot is in the lower-left or lower-right quarter
        is_lower_left = max_loc[0] < lower_half_width

        logging.debug("Brightness: %f", max_val)
        logging.debug("Is in lower-left quarter: %r", is_lower_left)


        return is_lower_left
