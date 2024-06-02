import requests
from dotenv import load_dotenv
import os
from typing import Dict, Any
import numpy as np

class ServiceNotHealthyError(Exception):
  """Exception raised when the service is not healthy."""
  def __init__(self, message="The client service is not healthy"):
    self.message = message
    super().__init__(self.message)

class Client:
    
    def __init__(self):
      load_dotenv()  
      self.server_ip: str = os.getenv('HOST')  
      self.server_port: int = int(os.getenv('PORT'))
      self.url: str = f'http://{self.server_ip}:{self.server_port}'
        
    def is_healthy(self) -> Dict[str, Any]:
      try:
        response = requests.get(self.url + '/is_healthy')
        return response.json()
      except Exception as e:
        raise ServiceNotHealthyError from e
      
    def get_image(self) -> Dict[str, Any]:
      response = requests.get(self.url + '/get_image')
      return response.json()
    
    def set_motor_speed(self, twentysix_delta: float, thirteen_delta: float) -> Dict[str, Any]:
      data = {
        "twentysix_delta": twentysix_delta,
        "thirteen_delta": thirteen_delta
      }
      response = requests.post(self.url + '/set_motor_speed', json=data)
      return response.json()