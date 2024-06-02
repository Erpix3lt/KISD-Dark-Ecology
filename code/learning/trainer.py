import random
from collections import deque
from environment import Environment
from model import DQN
import torch.nn as nn
import torch.optim as optim
import numpy as np
import torch
import time

def train():
  environment = Environment()
  model = DQN()
  optimizer = optim.Adam(model.parameters(), lr=0.001)
  criterion = nn.MSELoss()
  
  replay_memory = deque(maxlen=10000)
  batch_size = 32
  gamma = 0.99
  epsilon = 1.0
  epsilon_decay = 0.995
  epsilon_min = 0.01
    
  for episode in range(1000):
    state = environment.get_state()
    state = preprocess_state(state)
    total_reward = 0
    
    for t in range(200):
      if random.random() < epsilon:
        # RANDOM ACTION, EXPLORATIVE
        action = [random.uniform(-1, 1), random.uniform(-1, 1)]
      else:
        with torch.no_grad():
          # ESTIMATED ACTION, EXPLOITIVE
          action = model(torch.tensor(state, dtype=torch.float32)).numpy()
              
      next_state, reward, done = environment.step(action)
      time.sleep(1)
      next_state = preprocess_state(next_state)
      
      replay_memory.append((state, action, reward, next_state, done))
      state = next_state
      total_reward += reward
      
      if len(replay_memory) > batch_size:
        minibatch = random.sample(replay_memory, batch_size)
        for state_b, action_b, reward_b, next_state_b, done_b in minibatch:
          target = reward_b
          if not done_b:
              target += gamma * torch.max(model(torch.tensor(next_state_b, dtype=torch.float32)))
          
          output = model(torch.tensor(state_b, dtype=torch.float32))
          loss = criterion(output, torch.tensor(target, dtype=torch.float32))
          
          optimizer.zero_grad()
          loss.backward()
          optimizer.step()
      
      if done:
        break
    
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay
    
    print(f"Episode {episode + 1}: Total Reward: {total_reward}")

def preprocess_state(detections):
  """
  Preprocesses the detections to create a state representation.

  Args:
      detections (list): A list of Detection objects representing detected objects.

  Returns:
    list: A list representing the state, where each element corresponds to a feature of the state:
      - If the label of the object is 'cup' or 'car', the state is populated with the following information:
        - 1: Indicates the presence of the object.
        - detection.confidence: Confidence score of the detection.
        - detection.bounding_box[2]: Width of the bounding box of the detection.
        - detection.bounding_box[3]: Height of the bounding box of the detection.
      - If the label is not 'cup' or 'car', the corresponding state elements remain 0.
      - The resulting state list has a length of 8, where each group of 4 elements corresponds to a single object.
    """
  state = [0] * 8  
  for i, detection in enumerate(detections):
    if detection.label in ['person']:
      state[i * 4:(i + 1) * 4] = [1, detection.confidence, detection.bounding_box[2], detection.bounding_box[3]]
  return state

if __name__ == "__main__":
    train()
