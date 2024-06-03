import random
from collections import namedtuple, deque

class ReplayMemory(object):

    def __init__(self, capacity):
        self.Transition = namedtuple('Transition',
                        ('state', 'action', 'next_state', 'reward'))
        self.memory = deque([], maxlen=capacity)

    def push(self, *args):
        """Save a transition"""
        self.memory.append(self.Transition(*args))

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)