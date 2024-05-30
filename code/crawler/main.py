from vision_service import VisionService
from servo_service import ServoService
import logging
import time
from dotenv import load_dotenv
from distance_service import DistanceService
from client import Client
from PIL import Image
from typing import Dict, Any

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

    def run(self, where_to = 'cat'):
        is_healthy: Dict[str, Any] = self.client.is_healthy()  
        if is_healthy['result']:  
            while True:
                image: Image.Image = Image.fromarray(self.vision_service.capture_array())
                try: 
                    lead_to = self.client.lead_me_to(image, where_to)
                    if lead_to['result'] == 'RIGHT':
                        print("RIGHT")
                        self.servo_service.go_right()
                    if lead_to['result'] == 'LEFT':
                        print("LEFT")
                        self.servo_service.go_left()
                    if lead_to['result'] == 'UNKNOWN':
                        print("NOTHING DETECTED")
                    # if self.distance_analyser.is_Colliding():
                    #     logging.info("Collision detected. Stopping.")
                    #     self.servo_service.stop(duration=50)
                    #     self.servo_service.rotate(duration=50)
                except:
                    print("did not get back any response")
                time.sleep(5)
            

if __name__ == "__main__":
    crawler = Crawler()
    try:
        crawler.run()
    except KeyboardInterrupt:
        pass
    finally:
        crawler.stop()
       
