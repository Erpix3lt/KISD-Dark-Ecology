import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from detection_service import Detection_Service
from PIL import Image
from io import BytesIO
import base64
import tempfile
import webbrowser
from logger import Logger

class Server:
    def __init__(self):
        load_dotenv()
        self.app = Flask(__name__)
        self.port = int(os.getenv('PORT', 5500))
        self.host = os.getenv('HOST', '0.0.0.0')
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
        self.detection_service = Detection_Service()
        self.logger = Logger()
        
        @self.app.route('/is_healthy', methods=['GET'])
        def is_healthy():
            return jsonify({'is_running': True}), 200
        
        @self.app.route('/analyse_image', methods=['POST'])
        def analyse_image():
            data = request.get_json()
            image_data = data.get('image')
            try:
                image = Image.open(BytesIO(base64.b64decode(image_data)))
                result, analysed_image = self.detection_service.analyse_image(image)
                if self.log_level == 'DEBUG':
                    self.logger.log_analysed_image(analysed_image)        
                return jsonify({'result': str(result)}), 200
            except Exception as e:
                return jsonify({'error': f'There was an error while analysing the image: {str(e)}'}), 500
        
        @self.app.route('/lead_me_to', methods=['POST'])
        def lead_me_to():
            data = request.get_json()
            image_data = data.get('image')
            where_to = data.get('where_to')
            try:
                image = Image.open(BytesIO(base64.b64decode(image_data)))
                result, analysed_image = self.detection_service.analyse_image(image)
                if self.log_level == 'DEBUG':
                    self.logger.log_analysed_image(analysed_image)  
                direction = self.detection_service.navigate(image, result, where_to)
                if direction == 'unknown':
                    return jsonify({'error': 'There was an error while asserting the direction. The desired object might not have found.'}), 500
                return jsonify({'result': direction}), 200
            except Exception as e:
                return jsonify({'error': f'There was an error while analysing the image: {str(e)}'}), 500
        
    def run(self):
        self.app.run(host=self.host, port=self.port)  # Run server on all available IPs

if __name__ == '__main__':
    server = Server()
    server.run()
