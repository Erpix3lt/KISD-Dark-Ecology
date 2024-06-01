import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from client import Client
from detection_service import DetectionService
from logger import Logger
from servo_helper import ServoHelper
from PIL import Image
import base64
import io

# Define your reinforcement learning model using PyTorch
class PolicyNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(input_size, output_size)
        
    def forward(self, x):
        return torch.tanh(self.fc(x))

class Main:
    def __init__(self):
        # Your existing code
        self.client = Client()
        self.detection_service = DetectionService()
        self.logger = Logger()
        self.servo_helper = ServoHelper()
        self.reward_target = 'cup'

        # Define RL model
        self.state_size = 2  # You might need to adjust this based on your state representation
        self.action_size = 2  # Motor speeds for both motors
        self.policy_network = PolicyNetwork(self.state_size, self.action_size)
        self.optimizer = optim.Adam(self.policy_network.parameters(), lr=0.001)
        
    def base64_to_pil(self, base64_image: str) -> Image.Image:
      if ';base64,' in base64_image:
        base64_image = base64_image.split(';base64,')[-1]
      img_data = base64.b64decode(base64_image)
      img_stream = io.BytesIO(img_data)
      return Image.open(img_stream)
  
        
    def get_image(self) -> Image.Image:
      return self.base64_to_pil(self.client.get_image()['result'])

    def get_state(self, result):
        # Extract state from the detection result
        # For example, you might return the count of cups and cars detected
        data_frame = result.pandas().xyxy[0]
        desired_objects = data_frame[data_frame['name'] == self.reward_target]
        return len(desired_objects)

    def train(self, num_episodes):
        for episode in range(num_episodes):
            # Reset environment
            image = self.get_image()
            result, analysed_image = self.detection_service.analyse_image(image)
            state = self.get_state(result)

            done = False
            while not done:
                # Choose action
                with torch.no_grad():
                    action = self.policy_network(torch.FloatTensor(state))
                # Perform action and observe next state and reward
                # For simplicity, let's assume we send motor speeds directly as action
                motor_speeds = action.numpy()
                self.client.set_motor_speed(motor_speeds[0], motor_speeds[1])

                # Get new state and reward
                new_image = self.get_image()
                new_result, _ = self.detection_service.analyse_image(new_image)
                new_state = self.get_state(new_result)
                reward = self.calculate_reward(result, new_result)

                # Update policy
                self.optimize_model(state, action, reward, new_state)

                # Check if episode terminates
                done = False  # You need to define the termination condition

                # Update state
                state = new_state

    def calculate_reward(self, old_result, new_result):
        if any(target in new_result for target in self.reward_target):
            return 1  # Positive reward for finding target
        elif new_result == old_result:
            return -1  # Negative reward for no change (e.g., hitting a wall)
        else:
            return 0  # No reward or punishment

    def optimize_model(self, state, action, reward, new_state):
        # Compute loss
        predicted_action = self.policy_network(torch.FloatTensor(state))
        loss = -torch.log(predicted_action[action]) * reward

        # Optimize
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

if __name__ == "__main__":
    main = Main()
    main.train(num_episodes=1000)  # Train for 1000 episodes
