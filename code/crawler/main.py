from vision_service import VisionService
from brightness_analyser import BrightnessAnalyser
from servo_service import ServoService
import logging
import time
import os 
from dotenv import load_dotenv

class Crawler():
    def __init__(self):
        load_dotenv()
        self.vision_service = VisionService()
        self.brightness_analyser = BrightnessAnalyser()
        self.MUTE_SERVO = os.getenv("MUTE_SERVO", False)
        if not self.MUTE_SERVO:
            self.servo_service = ServoService()

    def start(self):
        self.vision_service.start()

    def stop(self):
        self.vision_service.close()
        if not self.MUTE_SERVO:
            self.servo_service.close()

    def run(self):
        while True:
            image = self.vision_service.capture_array()
            is_left = self.brightness_analyser.process_image(image)
            
            if is_left:
                logging.info("Bright spot is on the left.")
                if not self.MUTE_SERVO:
                    self.servo_service.go_left()
            else:
                logging.info("Bright spot is on the right.")
                if not self.MUTE_SERVO:
                    self.servo_service.go_right()

            time.sleep(2)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.start()
    try:
        crawler.run()
        # Implement scanning for the bright spot on the current position here. Should it exceed a certain threshold, stop the robot for some time.
    except KeyboardInterrupt:
        pass
    finally:
        crawler.stop()
       
