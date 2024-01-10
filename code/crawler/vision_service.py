from picamera2 import Picamera2
import logging

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

    def capture_array(self):
        logging.debug("Capturing image")
        return self.picam2.capture_array()

