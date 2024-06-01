from client import Client
from PIL import Image
from io import BytesIO
import base64
import io

class Main:
  
  def __init__(self):
    self.client = Client()
    
    self.twentysix_fast = -3.5
    self.twentysix_slow = -2
    self.twentysix_back = +0.7

    self.thirteen_fast = +2
    self.thirteen_slow = +0.5
    self.thirteen_back = -0.5
    
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
  image.show()
  main.client.set_motor_speed(0.5, 0.7)
  
    
