import torch
import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    """
    Neural network model for reinforcement learning.

    This model consists of three fully connected layers:
    - Input layer with 2 input features (object presence and bounding box size).
    - Two hidden layers with 128 units each, activated by ReLU.
    - Output layer with 2 units, representing the Q-values for the possible actions.
    """
    def __init__(self, n_input, n_actions):
        """
        Initializes the neural network layers.
        """
        super(DQN, self).__init__()
        self.layer1 = nn.Linear(n_input, 128)  
        self.layer2 = nn.Linear(128, 128)
        self.layer3 = nn.Linear(128, n_actions)
        
    def forward(self, x):
        """
        Performs a forward pass through the network.

        Args:
            x (Tensor): Input tensor of shape (batch_size, 2).

        Returns:
            Tensor: Output tensor of shape (batch_size, 2), representing actions for the servos.
        """
        x = F.relu(self.layer1(x))  
        x = F.relu(self.layer2(x))
        return self.layer3(x) 