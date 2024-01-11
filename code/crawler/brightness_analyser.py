import cv2
import logging
from logger import Logger

class BrightnessAnalyser:

    def process_image(self, image, analyse_lower_half=False):
        height, width = image.shape[:2]

        if analyse_lower_half:
            # Analyze only the lower half
            # Convert to grayscale
            gray_lower_half = cv2.cvtColor(image[height // 2 :, :], cv2.COLOR_BGR2GRAY)
            # Add Gaussian blur, to prevent noise mistakes
            gray_lower_half = cv2.GaussianBlur(gray_lower_half, (5, 5), 0)
            # Get max brightness value and location
            _, max_val, _, max_loc = cv2.minMaxLoc(gray_lower_half)
            lower_half_width = width // 2
            is_lower_left = max_loc[0] < lower_half_width
            logging.debug("Brightness: %f", max_val)
            logging.debug("Is in lower-left quarter: %r", is_lower_left)

            if logging.getLogger().isEnabledFor(logging.DEBUG):
                cv2.circle(image, (max_loc[0], max_loc[1] + height // 2), 10, (0, 0, 255), 2)
                cv2.line(image, (lower_half_width, 0), (lower_half_width, height), (255, 0, 0), 2)

            return is_lower_left, image

        else:
            # Analyze the complete image
            # Convert to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Add Gaussian blur, to prevent noise mistakes
            gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
            # Get max brightness value and location
            _, max_val, _, max_loc = cv2.minMaxLoc(gray_image)
            is_lower_left = max_loc[0] < width // 2
            logging.debug("Brightness: %f", max_val)
            logging.debug("Is in lower-left quarter: %r", is_lower_left)

            if logging.getLogger().isEnabledFor(logging.DEBUG):
                cv2.circle(image, max_loc, 10, (0, 0, 255), 2)
                cv2.line(image, (width // 2, 0), (width // 2, height), (255, 0, 0), 2)

            return is_lower_left, image
