from client import Client
from PIL import Image
import base64
import io
from detection_service import DetectionService, Detection
from logger import Logger
from servo_helper import ServoHelper
from typing import List
from logger import Logger

class Environment:
    def __init__(self):
        self.client = Client()
        self.client.is_healthy()
        self.detection_service = DetectionService()
        self.logger = Logger()
        self.servo_helper = ServoHelper()
        self.logger = Logger()
        
        self.reward_targets = ['person']
        
    def base64_to_pil(self, base64_image: str) -> Image.Image:
        if ';base64,' in base64_image:
            base64_image = base64_image.split(';base64,')[-1]
        img_data = base64.b64decode(base64_image)
        img_stream = io.BytesIO(img_data)
        return Image.open(img_stream)
    
    def get_image(self) -> Image.Image:
        return self.base64_to_pil(self.client.get_image()['result'])
    
    def get_state(self):
        image = self.get_image()
        result, analysed_image = self.detection_service.analyse_image(image)
        self.logger.log_analysed_image(analysed_image)
        detections: List[Detection] = self.detection_service.polish_result(result)
        return detections
    
    def compute_reward(self, detections):
      reward = 0
      if len(detections) == 0:
        reward = -1  
        print("NOTHING DETECTED, Reward:", reward)
      else:
        for detection in detections:
          if detection.label in self.reward_targets:
            reward = 1 
            print("DETECTED TARGET, Reward:", reward)
            break
          else:
            print("DETECTED SOMETHING ELSE, Reward:", reward)
      return reward
    
    def step(self, action):
        self.client.set_motor_speed(action[0], action[1])
        detections = self.get_state()
        reward = self.compute_reward(detections)
        # TODO: Implement done logic. In our case this might occur, when the robot has collided, reached its goal, or left its premise.
        done = False
        return detections, reward, done
