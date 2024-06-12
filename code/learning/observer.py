from client import Client
from detection_service import DetectionService
from PIL import Image
import base64
import io
from logger import Logger

class Observer():
  
  def __init__(self) -> None:
    self.client = Client()
    self.detection_service = DetectionService()
    self.logger = Logger()
    
  def base64_to_pil(self, base64_image: str) -> Image.Image:
      if ';base64,' in base64_image:
          base64_image = base64_image.split(';base64,')[-1]
      img_data = base64.b64decode(base64_image)
      img_stream = io.BytesIO(img_data)
      return Image.open(img_stream)
  
  def get_image(self) -> Image.Image:
        return self.base64_to_pil(self.client.get_image()['result'])
    
  def observe(self):
    image = self.get_image()
    result, analysed_image = self.detection_service.analyse_image(image)
    self.logger.log_analysed_image(analysed_image)
  
if __name__ == "__main__":
    observer = Observer()
    try:
        if observer.client.is_healthy:
          while True:
            observer.observe()
    except KeyboardInterrupt:
        print("Observer interrupted by the user.")
