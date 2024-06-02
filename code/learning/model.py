import torch.nn as nn
import torch
from typing import List

class Model(nn.Module):
    """
    Neural network model for reinforcement learning.

    This model consists of three fully connected layers:
    - Input layer with n_targets * 4 input features.
    - Two hidden layers with 128 units each, activated by ReLU.
    - Output layer with 2 units, representing the Q-values for the possible actions.

    Args:
        None

    Attributes:
        fc1 (nn.Linear): First fully connected layer.
        fc2 (nn.Linear): Second fully connected layer.
        fc3 (nn.Linear): Third fully connected layer.

    Methods:
        forward(x): Forward pass through the network.
    """
    def __init__(self):
        """
        Initializes the neural network layers.
        """
        super(Model, self).__init__()
        self.input_fields = 4
        self.fc1 = nn.Linear(2 * self.input_fields, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 2)
        
    def forward(self, x):
        """
        Performs a forward pass through the network.

        Args:
            x (Tensor): Input tensor of shape (batch_size, 8).

        Returns:
            Tensor: Output tensor of shape (batch_size, 2), representing Q-values for the actions.
        """
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
