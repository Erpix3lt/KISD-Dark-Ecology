import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

class MyFlaskApp:
    def __init__(self):
        load_dotenv()
        self.app = Flask(__name__)
        self.port = int(os.getenv('PORT', 5500))
        self.host = os.getenv('HOST', '0.0.0.0')
        
        @self.app.route('/is_healthy', methods=['GET'])
        def is_healthy():
            return jsonify({'is_running'}, 200)
        
        @self.app.route('/lead_me_to', methods=['POST'])
        def lead_me_to():
            data = request.get_json()
            image = data.get('image')
            to_where = data.get('to_where')
            

    def run(self):
        self.app.run(host=self.host, port=self.port)  # Run server on all available IPs

if __name__ == '__main__':
    my_app = MyFlaskApp()
    my_app.run()
