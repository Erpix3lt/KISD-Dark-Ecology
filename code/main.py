from vision_service import VisionService
from servo_service import ServoService
from logger import Logger
import logging
import time
from dotenv import load_dotenv
from distance_service import DistanceAnalyser

class Crawler():
    def __init__(self):
        load_dotenv()
        self.logger = Logger()
        self.vision_service = VisionService()
        self.vision_service.start()
        self.servo_service = ServoService()
        self.distance_analyser = DistanceAnalyser()
        
    def stop(self):
        self.vision_service.close()
        self.servo_service.close()

    def run(self):
        while True:
            image = self.vision_service.capture_array()
            if logging.DEBUG:
                self.logger.save_images_to_web_server(image)
            # if is_left:
            #     logging.info("Bright spot is on the left.")
            #     self.servo_service.go_left()
            # else:
            #     logging.info("Bright spot is on the right.")
            #     self.servo_service.go_right()
            if self.distance_analyser.is_Colliding():
                logging.info("Collision detected. Stopping.")
                self.servo_service.stop(duration=50)
                self.servo_service.rotate(duration=50)

if __name__ == "__main__":
    crawler = Crawler()
    try:
        crawler.run()
    except KeyboardInterrupt:
        pass
    finally:
        crawler.stop()
       
