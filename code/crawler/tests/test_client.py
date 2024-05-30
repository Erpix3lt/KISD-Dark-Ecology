import os
import sys
from typing import Dict, Any
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from client import Client
from vision_service import VisionService

client = Client()
vision_service = VisionService()
vision_service.start()

result: Dict[str, Any] = client.is_healthy()  
print(result)

image: Image.Image = Image.fromarray(vision_service.capture_array())
result = client.analyse_image(image)  
print(result)

image: Image.Image = Image.fromarray(vision_service.capture_array())
result = client.lead_me_to(image, 'vase')  
print(result)

vision_service.close()
