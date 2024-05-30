import requests
from dotenv import load_dotenv
import os
from vision_service import VisionService
from PIL import Image
from io import BytesIO
import base64

class Client:
    def __init__(self):
      load_dotenv()  
      self.server_ip = os.getenv('SERVER_IP')  
      self.server_port = int(os.getenv('SERVER_PORT'))
      self.url = f'http://{self.server_ip}:{self.server_port}'
      self.vision_service = VisionService()
        
    def is_healthy(self):
      response = requests.get(self.url + '/is_healthy')
      return response.json()
      
    def analyse_image(self, image: Image):
      buffered = BytesIO()
      image.save(buffered, format="JPEG")

      payload = {'image': base64.b64encode(buffered.getvalue()).decode('utf-8')}
      
      response = requests.post(self.url + '/analyse_image', json=payload)
      return response.json()

if __name__ == '__main__':
    client = Client()
    client.vision_service.start()

    result = client.is_healthy()  
    print(result)

    result = client.analyse_image(Image.fromarray(client.vision_service.capture_array()))  
    print(result)
    
    client.vision_service.close()
