from picamera2 import Picamera2, Preview
import time
picam2 = Picamera2()
picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")

class VisionService:

    def __init__(self):
        self.picam2 = Picamera2()

    def start(self):
        self.picam2.start()
        time.sleep(2)

    def stop(self):
        self.picam2.stop()
        self.picam2.close()

    def capture(self, filename):
        self.start()
        self.picam2.capture_file(filename)
        self.stop()

if __name__ == "__main__":
    vs = VisionService()
    vs.capture("test.jpg")