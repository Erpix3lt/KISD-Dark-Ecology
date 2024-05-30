import requests
from dotenv import load_dotenv
import os
from vision_service import VisionService

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
      
    def analyse_image(self):
      image = self.vision_service.capture_array()
      response = requests.post(self.url + '/analyse_image', image)
      return response.json()

if __name__ == '__main__':
    client = Client()
    result = client.is_healthy()  
    print(result)
    result = client.analyse_image()  
    print(result)
