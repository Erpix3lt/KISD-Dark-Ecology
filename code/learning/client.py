import requests
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO
import base64
from typing import Dict, Any

class Client:
    
    def __init__(self):
        load_dotenv()  
        self.server_ip: str = os.getenv('HOST')  
        self.server_port: int = int(os.getenv('PORT'))
        self.url: str = f'http://{self.server_ip}:{self.server_port}'
        
    def pil_to_base_64(self, image: Image.Image) -> str:
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        buffered: BytesIO = BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
        
    def is_healthy(self) -> Dict[str, Any]:
        response = requests.get(self.url + '/is_healthy')
        return response.json()
      
client = Client()
print(client.is_healthy())