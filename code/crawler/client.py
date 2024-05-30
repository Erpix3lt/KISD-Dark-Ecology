import requests
from dotenv import load_dotenv
import os
from vision_service import VisionService
from PIL import Image
from io import BytesIO
import base64
from typing import Dict, Any

class Client:
    def __init__(self):
        load_dotenv()  
        self.server_ip: str = os.getenv('SERVER_IP')  
        self.server_port: int = int(os.getenv('SERVER_PORT'))
        self.url: str = f'http://{self.server_ip}:{self.server_port}'
        self.vision_service: VisionService = VisionService()
        
    def pil_to_base_64(self, image: Image.Image) -> base64:
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        buffered: BytesIO = BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
        
    def is_healthy(self) -> Dict[str, Any]:
        response = requests.get(self.url + '/is_healthy')
        return response.json()
      
    def analyse_image(self, image: Image.Image) -> Dict[str, Any]:
        payload: Dict[str, str] = {'image': self.pil_to_base_64(image)}
        response = requests.post(self.url + '/analyse_image', json=payload)
        return response.json()
      
    def lead_me_to(self, image: Image.Image, where_to: str) -> Dict[str, Any]:
        payload: Dict[str, str] = {
            'image': self.pil_to_base_64(image),
            'where_to': where_to
        }
        response = requests.post(self.url + '/lead_me_to', json=payload)
        return response.json()

if __name__ == '__main__':
    client = Client()
    client.vision_service.start()

    result: Dict[str, Any] = client.is_healthy()  
    print(result)

    image: Image.Image = Image.fromarray(client.vision_service.capture_array())
    result = client.analyse_image(image)  
    print(result)
    
    client.vision_service.close()
