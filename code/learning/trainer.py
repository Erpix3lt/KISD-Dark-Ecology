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

class Trainer():
  
    def __init__(self) -> None:
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.environment = Environment('INFO')

        self.policy_net = DQN(n_input=self.environment.n_input, n_actions=self.environment.n_action).to(self.device)
        self.target_net = DQN(n_input=self.environment.n_input, n_actions=self.environment.n_action).to(self.device)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        
        self.memory = ReplayMemory(1000)
        self.Transition = self.memory.Transition
        self.optimizer = optim.AdamW(self.policy_net.parameters(), lr=LR, amsgrad=True)

        self.steps_done = 0
        
    def select_action(self, state):
      sample = random.random()
      eps_threshold = EPS_END + (EPS_START - EPS_END) * \
          math.exp(-1. * self.steps_done / EPS_DECAY)
      self.steps_done += 1
      if sample > eps_threshold:
        with torch.no_grad():
          # t.max(1) will return the largest column value of each row.
          # second column on max result is index of where max element was
          # found, so we pick action with the larger expected reward.
          return self.policy_net(state).max(1).indices.view(1, 1)
      else:
        return torch.tensor([[random.randrange(self.environment.n_action)]], device=self.device, dtype=torch.long)
          
    def optimize_model(self):
      if len(self.memory) < BATCH_SIZE:
          return
      transitions = self.memory.sample(BATCH_SIZE)
      # Transpose the batch (see https://stackoverflow.com/a/19343/3343043 for
      # detailed explanation). This converts batch-array of Transitions
      # to Transition of batch-arrays.
      batch = self.Transition(*zip(*transitions))

      # Compute a mask of non-final states and concatenate the batch elements
      # (a final state would've been the one after which simulation ended)
      non_final_mask = torch.tensor(tuple(map(lambda s: s is not None,
                                            batch.next_state)), device=self.device, dtype=torch.bool)
      non_final_next_states = torch.cat([s for s in batch.next_state
                                                  if s is not None])
      state_batch = torch.cat(batch.state)
      action_batch = torch.cat(batch.action)
      reward_batch = torch.cat(batch.reward)

      # Compute Q(s_t, a) - the model computes Q(s_t), then we select the
      # columns of actions taken. These are the actions which would've been taken
      # for each batch state according to policy_net
      state_action_values = self.policy_net(state_batch).gather(1, action_batch)

      # Compute V(s_{t+1}) for all next states.
      # Expected values of actions for non_final_next_states are computed based
      # on the "older" target_net; selecting their best reward with max(1).values
      # This is merged based on the mask, such that we'll have either the expected
      # state value or 0 in case the state was final.
      next_state_values = torch.zeros(BATCH_SIZE, device=self.device)
      with torch.no_grad():
          next_state_values[non_final_mask] = self.target_net(non_final_next_states).max(1).values
      # Compute the expected Q values
      expected_state_action_values = (next_state_values * GAMMA) + reward_batch

      # Compute Huber loss
      criterion = nn.SmoothL1Loss()
      loss = criterion(state_action_values, expected_state_action_values.unsqueeze(1))

      # Optimize the model
      self.optimizer.zero_grad()
      loss.backward()
      # In-place gradient clipping
      torch.nn.utils.clip_grad_value_(self.policy_net.parameters(), 100)
      self.optimizer.step()
    
    def train(self):
        if torch.cuda.is_available():
            num_episodes = 600
            print(f"CUDA IS AVAILABLE, num of episodes {num_episodes}")
        else:
            num_episodes = 50
            print(f"CUDA NOT AVAILABLE, num of episodes {num_episodes}")

        for i_episode in range(num_episodes):
            print(f"EPISODE {i_episode}")
            # Initialize the environment and get its state
            state = self.environment.reset()
            state = torch.tensor(state, dtype=torch.float32, device=self.device).unsqueeze(0)
            for t in count():
                action = self.select_action(state)
                print("ACTION:", int(action.item()))
                observation, reward, terminated = self.environment.step(int(action.item()), duration=0.2)
                print(f"Observation: {observation}, Reward {reward}, terminated: {terminated}")
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
                
                if terminated:
                  break

        print('Complete')

if __name__ == "__main__":
    trainer = Trainer()
    try:
        trainer.train()
        save_dir = "./_saved_models"
        os.makedirs(save_dir, exist_ok=True)
        torch.save(trainer.policy_net.state_dict(), os.path.join(save_dir, "trained_model.pth"))
    except KeyboardInterrupt:
        print("Training interrupted by the user.")
