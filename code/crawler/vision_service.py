from picamera2 import Picamera2
import logging
import numpy as np

class VisionService:
    def __init__(self):
        self.picam2 = Picamera2()

    def start(self):
        self.picam2.start()
        logging.debug("Camera started")

    def close(self):
        self.picam2.stop()
        self.picam2.close()
        logging.debug("Camera stopped")

    def capture_array(self, flip_image = True):
        logging.debug("Capturing image")
        original_image = self.picam2.capture_array()
        if flip_image:
            return np.fliplr(np.flipud(original_image))
        else:
            return original_image


