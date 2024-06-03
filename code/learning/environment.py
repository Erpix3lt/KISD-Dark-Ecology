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
import time

class Reward:
  def __init__(self) -> None:
    load_dotenv()
    self.targets = os.getenv('TARGETS').split(',')
    self.treat = 1
    self.normalization_factor = 9000
    self.punishment = -5

class Environment:
    def __init__(self, log_level = 'INFO'):
      self.client = Client()
      self.client.is_healthy()
      self.detection_service = DetectionService()
      self.log_level = log_level
      self.logger = Logger()
      self.servo_helper = ServoHelper()
      self.approach_treshold = 50000
      self.reward = Reward()
      self.n_input = 2
      self.n_action = 9

    def reset(self):
      self.state = [0, 0]
      return self.state
    
    def base64_to_pil(self, base64_image: str) -> Image.Image:
      if ';base64,' in base64_image:
          base64_image = base64_image.split(';base64,')[-1]
      img_data = base64.b64decode(base64_image)
      img_stream = io.BytesIO(img_data)
      return Image.open(img_stream)
  
    def get_image(self) -> Image.Image:
        return self.base64_to_pil(self.client.get_image()['result'])
    
    def get_detections(self) -> List[Detection]:
      image = self.get_image()
      result, analysed_image = self.detection_service.analyse_image(image)
      if self.log_level == 'DEBUG':
        self.logger.log_analysed_image(analysed_image)
      return self.detection_service.polish_result(result)

    def step(self, action: int, duration = 1):
      twentysix_delta, thirteen_delta = self.servo_helper.map_action_to_motor_speeds(action)
      self.client.set_motor_speed(twentysix_delta, thirteen_delta)
      time.sleep(duration)
      detections = self.get_detections()
      if self.log_level == 'DEBUG':
        print("Detections: ", detections)
        
      reward: int = self.compute_reward(detections)
      terminated: bool = self.check_done(detections) 
      observation = (0, 0)
    
      for detection in detections:
          if detection.label in self.reward.targets:
              object_presence = 1
              object_box_size = ((detection.bounding_box[2] - detection.bounding_box[0]) * (detection.bounding_box[3] - detection.bounding_box[1]))
              observation = (object_presence, object_box_size)
      
      return observation, reward, terminated

    def compute_reward(self, detections: List[Detection]) -> int:
      reward = self.reward.punishment
      for detection in detections:
        if detection.label in self.reward.targets:
          box_size = (detection.bounding_box[2] - detection.bounding_box[0]) * (detection.bounding_box[3] - detection.bounding_box[1])
          reward = self.reward.treat * (box_size / self.reward.normalization_factor)
          break        
      if self.log_level == "DEBUG":
        print('Reward:', reward)
      return reward

    def check_done(self, detections: List[Detection]) -> bool:
      """
      Check wether the robot has approached the desired object sufficiently. If so return true. Our run is done. If not return false, continue.
      """
      is_done = False
      for detection in detections:
        if detection.label in self.reward.targets:
          box_size = (detection.bounding_box[2] - detection.bounding_box[0]) * (detection.bounding_box[3] - detection.bounding_box[1])
          if box_size > self.approach_treshold:
            is_done = True
      return is_done
          


