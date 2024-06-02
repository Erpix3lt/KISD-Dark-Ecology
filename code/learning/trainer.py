import random
from collections import deque
from environment import Environment, Reward
from model import Model
import torch.nn as nn
import torch.optim as optim
import torch
import time
import os

class Trainer():
  
  def __init__(self) -> None:
    self.environment = Environment()
    self.reward = Reward()
    self.model = Model(self.reward.targets)
    self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
    self.criterion = nn.MSELoss()
    
    self.replay_memory = deque(maxlen=10000)
    self.batch_size = 32
    self.gamma = 0.99
    self.epsilon = 1.0
    self.epsilon_decay = 0.995
    self.epsilon_min = 0.01
    
    self.episodes = 1
    self.steps = 2

  def train(self): 
    for episode in range(self.episodes):
      state = self.environment.get_state()
      state = self.preprocess_state(state)
      total_reward = 0
      
      for t in range(self.steps):
        if random.random() < self.epsilon:
          # RANDOM ACTION, EXPLORATIVE
          action = [random.uniform(-1, 1), random.uniform(-1, 1)]
        else:
          with torch.no_grad():
            # ESTIMATED ACTION, EXPLOITIVE
            action = self.model(torch.tensor(state, dtype=torch.float32)).numpy()
                
        next_state, reward, done = self.environment.step(action)
        time.sleep(1)
        next_state = self.preprocess_state(next_state)
        
        self.replay_memory.append((state, action, reward, next_state, done))
        state = next_state
        total_reward += reward
        
        if len(self.replay_memory) > self.batch_size:
          minibatch = random.sample(self.replay_memory, self.batch_size)
          for state_b, action_b, reward_b, next_state_b, done_b in minibatch:
            target = reward_b
            if not done_b:
                target += self.gamma * torch.max(self.model(torch.tensor(next_state_b, dtype=torch.float32)))
            
            output = self.model(torch.tensor(state_b, dtype=torch.float32))
            loss = self.criterion(output, torch.tensor(target, dtype=torch.float32))
            
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        
        if done:
          break
      
      if self.epsilon > self.epsilon_min:
          self.epsilon *= self.epsilon_decay
      
      print(f"Episode {episode + 1}: Total Reward: {total_reward}")

  def preprocess_state(self, detections):
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
    state = [0] * (len(self.reward.targets) * self.model.input_fields)
    for i, detection in enumerate(detections):
      if detection.label in self.reward.targets:
        state[i * self.model.input_fields:(i + 1) * self.model.input_fields] = [1, detection.confidence, detection.bounding_box[2], detection.bounding_box[3]]
    return state

if __name__ == "__main__":
  trainer = Trainer()
  try:
    trainer.train()
    save_dir = "./_saved_models"
    os.makedirs(save_dir, exist_ok=True)
    torch.save(trainer.model.state_dict(), os.path.join(save_dir, "trained_model.pth"))

  except KeyboardInterrupt:
    print("Training interrupted by the user.")
