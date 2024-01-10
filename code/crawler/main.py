from vision_service import VisionService
from brightness_analyser import BrightnessAnalyser
from servo_service import ServoService
import argparse
import logging

def parse_args():
    parser = argparse.ArgumentParser(description='Process images and control servos based on brightness analysis.')
    parser.add_argument('--no_servo', action='store_true', help='Disable servo movement')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    vision_service = VisionService()
    vision_service.start()
    brightness_analyser = BrightnessAnalyser()
    if not args.no_servo:
        servo_service = ServoService()

    try:
        while True:
            image = vision_service.capture_array()
            is_left = brightness_analyser.process_image(image)
            
            if is_left:
                logging.warn("Bright spot is on the left.")
                if not args.no_servo:
                    logging.debug("Now moving towards the left.")
                    servo_service.go_left()
                    logging.debug("Finished moving towards the left.")
            else:
                logging.warn("Bright spot is on the right.")
                if not args.no_servo:
                    logging.debug("Now moving towards the right.")
                    servo_service.go_right()
                    logging.debug("Finished moving towards the right.")

            # Implement scanning for the bright spot on the current position here. Should it exceed a certain threshold, stop the robot for some time.
    except KeyboardInterrupt:
        pass
    finally:
        vision_service.stop()
        if not args.no_servo:
            servo_service.stop()
