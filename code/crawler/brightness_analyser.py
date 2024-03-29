import cv2
import logging
from numpy.linalg import norm
import numpy as np

class BrightnessAnalyser:

    def __init__(self, images: []):
        # analyse the overall brightness of all images in the array and calculate the average, this should be the baseline brightness
        self.baseline_brightness = 0
        for image in images:
            self.baseline_brightness += self.analyse_overall_brightness(image)
        self.baseline_brightness = self.baseline_brightness / len(images)
        logging.debug("Baseline brightness: %f", self.baseline_brightness)
        self.mulitplier = 1.5

    def process_image(self, image, analyse_lower_half=False, blur_kernel_size=(5, 5), blur_sigma=0):
        height, width = image.shape[:2]
        if analyse_lower_half:
            image = cv2.cvtColor(image[height // 2 :, :], cv2.COLOR_BGR2GRAY)
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Add Gaussian blur, to prevent noise mistakes
        image = cv2.GaussianBlur(image, blur_kernel_size, blur_sigma)
        _, max_val, _, max_loc = cv2.minMaxLoc(image)
        half_width = width // 2
        is_left = max_loc[0] < half_width
        logging.debug("Brightness: %f", max_val)
        logging.debug("Is in lower-left quarter: %r", is_left)

        if logging.getLogger().isEnabledFor(logging.DEBUG):
            cv2.circle(image, (max_loc[0], max_loc[1] + height // 2), 10, (255, 0, 0), 2)
            cv2.line(image, (half_width, 0), (half_width, height), (255, 0, 0), 2)

        return is_left, image
    
    def analyse_overall_brightness(self, image) :
        if len(image.shape) == 3:
            # Colored RGB or BGR (*Do Not* use HSV images with this function)
            # create brightness with euclidean norm
            return np.average(norm(image, axis=2)) / np.sqrt(3)
        else:
            # Grayscale
            return np.average(image)
        
    
    def check_if_above_treshold(self, image, treshold = None):
        if treshold == None:
            treshold = self.baseline_brightness * self.mulitplier
        current_brightness = self.analyse_overall_brightness(image)
        logging.debug("Current brightness: %f", current_brightness)
        if current_brightness > treshold:
            logging.debug("Current brightness is " + str(current_brightness) + " and is above threshold " + str(treshold))
            return True
        else:
            logging.debug("Current brightness is " + str(current_brightness) + " and is below threshold " + str(treshold))
            return False

        