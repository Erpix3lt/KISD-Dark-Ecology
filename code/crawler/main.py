from vision_service import VisionService
from brightness_analyser import BrightnessAnalyser
from servo_service import ServoService
import time

if __name__ == "__main__":
    vision_service = VisionService()
    brightness_analyser = BrightnessAnalyser()
    servo_service = ServoService()

    vision_service.start()

    try:
        while True:
            image = vision_service.capture_array()
            is_left = brightness_analyser.process_image(image)
            
            if is_left:
                print("Bright spot is on the left.")
                print("Now moving towards the left.")
                servo_service.move_left()
                print("Finished moving towards the left.")
            else:
                print("Bright spot is on the right.")
                print("Now moving towards the right.")
                servo_service.move_right()
                print("Finished moving towards the right.")

            # Implement scanning for the bright spot on the current position here. Should it exveed a certain treshold, stop the robot for some time.
    except KeyboardInterrupt:
        pass
    finally:
        vision_service.stop()
        servo_service.stop()
