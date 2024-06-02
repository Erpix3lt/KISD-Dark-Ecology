from client import Client
from PIL import Image
import base64
import io
from detection_service import DetectionService, Detection
from logger import Logger
from servo_helper import ServoHelper
from typing import List
from logger import Logger
import os
from dotenv import load_dotenv
from servo_helper import ServoHelper

class Reward():
  
  def __init__(self) -> None:
    load_dotenv()
    self.targets = os.getenv('TARGETS').split(',')
    self.treat = 1
    self.punishment = -5
    self.normalization_factor = 10000
    self.servo_helper = ServoHelper()

class Environment:
  def __init__(self, log_level = 'INFO'):
    self.client = Client()
    self.client.is_healthy()
    self.detection_service = DetectionService()
    self.logger = Logger()
    self.servo_helper = ServoHelper()
    self.logger = Logger()
    self.reward = Reward()
    self.log_level = log_level
        
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
      if self.log_level == 'DEBUG':
        self.logger.log_analysed_image(analysed_image)
      detections: List[Detection] = self.detection_service.polish_result(result)
      return detections
  
  def compute_reward(self, detections):
    reward = self.reward.punishment
    for detection in detections:
      if detection.label in self.reward.targets:
        box_size = (detection.bounding_box[2] - detection.bounding_box[0]) * (detection.bounding_box[3] - detection.bounding_box[1])
        reward = self.reward.treat * (box_size / self.reward.normalization_factor)
        break        
    print("Reward:", reward)
    return reward
  
  def step(self, action):
    self.client.set_motor_speed(self.servo_helper.get_twentysix_delta(action[0]), self.servo_helper.get_thirteen_delta(action[1]))
    detections = self.get_state()
    print("DETECTIONS:", detections)
    reward = self.compute_reward(detections)
    # TODO: Implement done logic. In our case this might occur, when the robot has collided, reached its goal, or left its premise.
    done = False
    return detections, reward, done
