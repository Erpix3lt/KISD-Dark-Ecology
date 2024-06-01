import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from vision_service import VisionService
from servo_service import ServoService
from PIL import Image
from io import BytesIO
import base64
import logging

class Server:
    def __init__(self):
      load_dotenv()
      self.logger = logging.getLogger(__name__)
      self.logger.setLevel(logging.INFO)
      self.app = Flask(__name__)
      self.port = int(os.getenv('PORT', 5500))
      self.host = os.getenv('HOST', '0.0.0.0')
      self.vision_service = VisionService()
      self.vision_service.start()
      self.servo_service = ServoService(logger)
      
      @self.app.route('/is_healthy', methods=['GET'])
      def is_healthy():
          return jsonify({'result': True}), 200
      
      @self.app.route('/get_image', methods=['GET'])  
      def get_image():
        try:
          image: Image.Image = Image.fromarray(self.vision_service.capture_array())
          base64_image = self.pil_to_base_64(image)
          return  jsonify({'result': base64_image}), 200
        except Exception as e:
          return jsonify({'error': f'Error retrieving image from server: {e}'}), 500 
        
      @self.app.route('/set_motor_speed', methods=['POST'])   
      def set_motor_speed():
        try:
          data = request.get_json()
          if not data or 'twentysix_delta' not in data or 'thirteen_delta' not in data:
            return jsonify({'error': 'Invalid input data'}), 400
          
          self.servo_service.set_motor_speed(data['twentysix_delta'], data['thirteen_delta'])
          return jsonify({'result': 'Motor speed set successfully'}), 200
        except Exception as e:
          return jsonify({'error': f'Error setting motor speed: {e}'}), 500
        
      @self.app.route('/clean_up', methods=['POST'])
      def clean_up():
        try:
          self.vision_service.close()
          self.servo_service.close()
          return jsonify({'result': 'Clean up was successfull'}), 200
        except Exception as e:
          return jsonify({'error:' f'Error cleaning up: {e}'}), 500

        
    def pil_to_base_64(self, image: Image.Image) -> str:
      if image.mode == 'RGBA':
          image = image.convert('RGB')
      buffered: BytesIO = BytesIO()
      image.save(buffered, format="JPEG")
      return base64.b64encode(buffered.getvalue()).decode('utf-8')
                
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == '__main__':
    server = Server()
    server.run()