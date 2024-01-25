from vision_service import VisionService
from brightness_analyser import BrightnessAnalyser
from servo_service import ServoService
from logger import Logger
import logging
import time
from dotenv import load_dotenv

class Crawler():
    def __init__(self):
        load_dotenv()
        self.logger = Logger()
        self.vision_service = VisionService()
        self.brightness_analyser = BrightnessAnalyser(self.caputere_baseline_images())
        self.servo_service = ServoService()

    def caputere_baseline_images(self, quantity=5):
        images = []
        images.extend(self.vision_service.capture_array() for _ in range(quantity))
        for image in images:
            self.logger.save_images_to_web_server(image, tag="BASELINE")
        return images

    def start(self):
        self.vision_service.start()

    def stop(self):
        self.vision_service.close()
        self.servo_service.close()

    def run(self):
        while True:
            print("is Logging debiúg:" , logging.DEBUG)
            image = self.vision_service.capture_array()
            is_left, image = self.brightness_analyser.process_image(image)
            if logging.DEBUG:
                self.logger.save_images_to_web_server(image)
            if is_left:
                logging.info("Bright spot is on the left.")
                self.servo_service.go_left()
            else:
                logging.info("Bright spot is on the right.")
                self.servo_service.go_right()
            if self.brightness_analyser.check_if_above_treshold(image):
                logging.info("Bright spot is above threshold.")
                self.servo_service.stop(duration=50)
                self.servo_service.rotate(duration=50)

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
       
