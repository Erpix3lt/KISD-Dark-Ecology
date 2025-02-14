# Deep reinforcement learning
During the project, we encountered a scenario that prompted us to implement deep reinforcement learning.

The task at hand is to guide a robot towards desired objects, which, for simplicity, could be an apple or a banana. The robot is equipped with a Raspberry Pi, a camera, and two imprecise 360° servo motors that control its legs. Due to the imprecision of these servo motors, achieving predetermined movements accurately is challenging, and moving forward directly is not feasible. Consequently, we decided to implement deep reinforcement learning.

The Raspberry Pi, with its camera, acts as a server. The PC running the learning script can communicate with the Raspberry Pi through the following requests: get_image, which retrieves the current image, and set_servo_speed, which adjusts the desired servo speed. The script is equipped with YOLOv5 object detection, capable of recognizing objects rapidly. Our objective is to reward the model based on the presence of desired objects (apples and bananas) within the image frame. The reward increases proportionally with the size of the objects in the frame, indicating the robot's approach towards them. Currently, the model receives input values in the following format for each detected object: (Boolean indicating presence, bounding box size).

Our aim is for the model to learn to associate the reward with the distance and type of the desired object.

## References
- https://chatgpt.com/share/d0b5e154-b9e0-4a49-950b-adbfc1d4d0ca
- Intro Deep Reinforcement learning: https://www.youtube.com/watch?v=cO5g5qLrLSo
- Doc, pytorch DQN deep reinforcement learning: https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
- https://discuss.pytorch.org/t/very-simple-environment-with-continuous-action-space-fails-to-learn-effectively-with-ppo/182397/8

## Key Learnings
1. In a Deep Q-Network (DQN) approach, the following components are essential:

- Actions
- Rewards
- Environment
- Agent

2. Discrete vs. continuous actions:

- Discrete actions are predefined actions. In our case, motor fast, motor slow, motor backwards
- Continuous actions present the model with a stream of choices. Motor +98% Speed, motor -50% speed.
