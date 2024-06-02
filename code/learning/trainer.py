import os
from replay_memory import ReplayMemory
from model import DQN
import math
import random
from itertools import count
from environment import Environment

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

BATCH_SIZE = 128
GAMMA = 0.99
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 1000
TAU = 0.005
LR = 1e-4

class TrainerV():
  
  def __init__(self) -> None:
    self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    self.policy_net = DQN(n_input = 2, n_actions = 2).to(self.device)
    self.target_net = DQN(n_input = 2, n_actions = 2).to(self.device)
    self.target_net.load_state_dict(self.policy_net.state_dict())
    
    self.environment = Environment()
    self.memory = ReplayMemory(1000)
    self.Transition = self.memory.Transition
    self.optimizer = optim.AdamW(self.policy_net.parameters(), lr=LR, amsgrad=True)

    self.steps_done: int = 0
    
  def select_action(self, state):
    sample = random.random()
    eps_threshold = EPS_END + (EPS_START - EPS_END) * \
      math.exp(-1. * self.steps_done / EPS_DECAY)
    self.steps_done += 1
    if sample > eps_threshold:
      with torch.no_grad():
        return self.policy_net(state).max(1)[1].view(1, 1)    
    else:
      return torch.tensor([[random.randrange(self.output_dim)]], dtype=torch.long)
    
  def optimize_model(self):
    if len(self.memory) < BATCH_SIZE:
        return
    transitions = self.memory.sample(BATCH_SIZE)
    batch = self.Transition(*zip(*transitions))
    non_final_mask = torch.tensor(tuple(map(lambda s: s is not None,
                                          batch.next_state)), device=self.device, dtype=torch.bool)
    non_final_next_states = torch.cat([s for s in batch.next_state
                                                if s is not None])
    state_batch = torch.cat(batch.state)
    action_batch = torch.cat(batch.action)
    reward_batch = torch.cat(batch.reward)
    state_action_values = self.policy_net(state_batch).gather(1, action_batch)

    next_state_values = torch.zeros(BATCH_SIZE, device=self.device)
    with torch.no_grad():
        next_state_values[non_final_mask] = self.target_net(non_final_next_states).max(1).values
    expected_state_action_values = (next_state_values * GAMMA) + reward_batch

    criterion = nn.SmoothL1Loss()
    loss = criterion(state_action_values, expected_state_action_values.unsqueeze(1))

    self.optimizer.zero_grad()
    loss.backward()
    torch.nn.utils.clip_grad_value_(self.policy_net.parameters(), 100)
    self.optimizer.step()
    
  def train(self):
    if torch.cuda.is_available():
      num_episodes = 600
    else:
        num_episodes = 50

    for i_episode in range(num_episodes):
        # Initialize the environment and get its state
        state = self.environment.reset()
        state = torch.tensor(state, dtype=torch.float32, device=self.device).unsqueeze(0)
        for t in count():
            action = self.select_action(state)
            print("Action, ", action)
            observation, reward, terminated = self.environment.step(action.item())
            reward = torch.tensor([reward], device=self.device)

            if terminated:
                next_state = None
            else:
                next_state = torch.tensor(observation, dtype=torch.float32, device=self.device).unsqueeze(0)

            # Store the transition in memory
            self.memory.push(state, action, next_state, reward)

            # Move to the next state
            state = next_state

            # Perform one step of the optimization (on the policy network)
            self.optimize_model()

            # Soft update of the target network's weights
            # θ′ ← τ θ + (1 −τ )θ′
            target_net_state_dict = self.target_net.state_dict()
            policy_net_state_dict = self.policy_net.state_dict()
            for key in policy_net_state_dict:
                target_net_state_dict[key] = policy_net_state_dict[key]*TAU + target_net_state_dict[key]*(1-TAU)
            self.target_net.load_state_dict(target_net_state_dict)

    print('Complete')

if __name__ == "__main__":
  trainer = TrainerV()
  try:
    trainer.train()
    save_dir = "./_saved_models"
    os.makedirs(save_dir, exist_ok=True)
    torch.save(trainer.model.state_dict(), os.path.join(save_dir, "trained_model.pth"))

  except KeyboardInterrupt:
    print("Training interrupted by the user.")
