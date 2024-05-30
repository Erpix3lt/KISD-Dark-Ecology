from vision_service import VisionService
from servo_service import ServoService
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
        self.previous_lead_to = None
        
    def stop(self):
        self.vision_service.close()
        self.servo_service.close()
        
    def handle_unknown(self):
        if self.previous_lead_to is not None:
            if self.previous_lead_to == 'RIGHT':
                print("RIGHT")
                self.servo_service.go_right()
            elif self.previous_lead_to == 'LEFT':
                print("LEFT")
                self.servo_service.go_left()
            elif self.previous_lead_to == 'UNKNOWN':
                print("ROTATING")
                self.servo_service.rotate(5)
        else:
            print("Previous lead to not yet define")
            
    def handle_is_colliding(self):
        print("Collision detected. Stopping.")
        self.servo_service.stop(duration=50)
        self.servo_service.rotate(duration=50)

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
                        self.handle_unknown()
                    # if self.distance_analyser.is_Colliding():
                    #     self.handle_is_colliding()
                except Exception as e:
                    print("NO RESPONSE GIVEN", str(e))
                self.previous_lead_to = lead_to
                time.sleep(5)

if __name__ == "__main__":
    crawler = Crawler()
    try:
        crawler.run()
    except KeyboardInterrupt:
        pass
    finally:
        crawler.stop()
       
