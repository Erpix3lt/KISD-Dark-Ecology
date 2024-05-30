from vision_service import VisionService
from servo_service import ServoService
import logging
import time
from dotenv import load_dotenv
from distance_service import DistanceService
from client import Client
from PIL import Image

class Crawler():
    def __init__(self):
        load_dotenv()
        self.vision_service = VisionService()
        self.vision_service.start()
        self.servo_service = ServoService()
        #self.distance_analyser = DistanceService()
        self.client = Client()
        
    def stop(self):
        self.vision_service.close()
        self.servo_service.close()

    def run(self):
        while True:
            image: Image.Image = Image.fromarray(self.vision_service.capture_array())
            result = self.client.lead_me_to(image, 'vase')
            if result == 'RIGHT':
                self.servo_service.go_right()
            if result == 'LEFT':
                self.servo_service.go_left()
            if result == 'UNKNOWN':
                logging.info("NOTHING DETECTED")
            # if self.distance_analyser.is_Colliding():
            #     logging.info("Collision detected. Stopping.")
            #     self.servo_service.stop(duration=50)
            #     self.servo_service.rotate(duration=50)

if __name__ == "__main__":
    crawler = Crawler()
    try:
        crawler.run()
    except KeyboardInterrupt:
        pass
    finally:
        crawler.stop()
       
