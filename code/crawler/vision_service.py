from picamera2 import Picamera2

class VisionService:
    def __init__(self):
        self.picam2 = Picamera2()

    def start(self):
        self.picam2.start()

    def stop(self):
        self.picam2.stop()
        self.picam2.close()

    def capture_array(self):
        return self.picam2.capture_array()
