from client import Client
from PIL import Image
import base64
import io
from detection_service import DetectionService, Detection
from logger import Logger
from servo_helper import ServoHelper
from typing import List

class Main:
  
  def __init__(self):
    self.client = Client()
    self.client.is_healthy()
    self.detection_service = DetectionService()
    self.logger = Logger()
    self.servo_helper = ServoHelper()
    
    self.reward_targets = ['cup', 'car']
    
  def base64_to_pil(self, base64_image: str) -> Image.Image:
    if ';base64,' in base64_image:
      base64_image = base64_image.split(';base64,')[-1]
    img_data = base64.b64decode(base64_image)
    img_stream = io.BytesIO(img_data)
    return Image.open(img_stream)
  
  def get_image(self) -> Image.Image:
    return self.base64_to_pil(self.client.get_image()['result'])
  
if __name__ == "__main__":
  main = Main()
  image = main.get_image()
  result, analysed_image = main.detection_service.analyse_image(image)
  detections: List[Detection] = main.detection_service.polish_result(result)
  for detection in detections:
    print(detection)
  main.logger.log_analysed_image(analysed_image)
  main.client.set_motor_speed(main.servo_helper.get_twentysix_delta(0.5), main.servo_helper.get_thirteen_delta(-0.5))
  
    
