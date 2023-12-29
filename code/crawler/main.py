from vision_service import VisionService
from brightness_analyser import BrightnessAnalyser
import time

if __name__ == "__main__":
    vs = VisionService()
    brightness_analyser = BrightnessAnalyser()

    vs.start()

    try:
        while True:
            image = vs.capture_array()
            is_left = brightness_analyser.process_image(image)
            
            if is_left:
                print("Left")
            else:
                print("Right")

            time.sleep(2) 
    except KeyboardInterrupt:
        pass
    finally:
        vs.stop()
