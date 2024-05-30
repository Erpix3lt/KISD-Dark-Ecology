from picamera2 import Picamera2
import numpy as np

class VisionService:
    
    def __init__(self):
        self.picam2: Picamera2 = Picamera2()

    def start(self) -> None:
        self.picam2.start()

    def close(self) -> None:
        self.picam2.stop()
        self.picam2.close()

    def capture_array(self, flip_image: bool = True) -> np.ndarray:
        original_image: np.ndarray = self.picam2.capture_array()
        if flip_image:
            return np.fliplr(np.flipud(original_image))
        else:
            return original_image
