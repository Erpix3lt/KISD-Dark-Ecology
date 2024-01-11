import cv2
import logging
from logger import Logger

class BrightnessAnalyser:

    def process_image(self, image, analyse_lower_half=False, blur_kernel_size=(5, 5), blur_sigma=0):
        height, width = image.shape[:2]

        if analyse_lower_half:
            image = cv2.cvtColor(image[height // 2 :, :], cv2.COLOR_BGR2GRAY)
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Add Gaussian blur, to prevent noise mistakes
        image = cv2.GaussianBlur(image, blur_kernel_size, blur_sigma)
        _, max_val, _, max_loc = cv2.minMaxLoc(image)
        lower_half_width = width // 2
        is_lower_left = max_loc[0] < lower_half_width
        logging.debug("Brightness: %f", max_val)
        logging.debug("Is in lower-left quarter: %r", is_lower_left)

        if logging.getLogger().isEnabledFor(logging.DEBUG):
            cv2.circle(image, (max_loc[0], max_loc[1] + height // 2), 10, (0, 0, 255), 2)
            cv2.line(image, (lower_half_width, 0), (lower_half_width, height), (255, 0, 0), 2)

        return is_lower_left, image