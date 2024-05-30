import requests
from dotenv import load_dotenv
import os

class Client:
    def __init__(self):
        load_dotenv()  
        self.server_ip = os.getenv('SERVER_IP')  
        self.server_port = os.getenv('SERVER_PORT')
        self.url = f'http://{self.server_ip}:{self.server_port}'
        
    def is_healthy(self):
      response = requests.get(self.url + '/is_healthy')
      return response.json()

if __name__ == '__main__':
    client = Client()
    result = client.is_healthy()  # Send numbers 3 and 4 to the server
    print(result)
