import requests
from dotenv import load_dotenv
import os

class Client:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.server_ip = os.getenv('SERVER_IP')  # Retrieve SERVER_IP from environment variables
        self.url = f'http://{self.server_ip}:5000'  # Construct the URL for the add endpoint

    def post_add(self, a, b):
        payload = {'a': a, 'b': b}  # Data to send in the request
        response = requests.post(self.url + '/add', json=payload)  # Send POST request
        return response.json()  # Return the server response

# Example usage
if __name__ == '__main__':
    client = Client()
    result = client.post_add(3, 4)  # Send numbers 3 and 4 to the server
    print(result)
