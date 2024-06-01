class ServoHelper:
  def __init__(self):
    self.twentysix_speed = -3.5
    self.thirteen_speed = 2
    
    # self.twentysix_fast = -3.5
    # self.twentysix_slow = -2
    # self.twentysix_back = +0.7

    # self.thirteen_fast = +2
    # self.thirteen_slow = +0.5
    # self.thirteen_back = -0.5
      
  def get_twentysix_delta(self, percentage: float) -> float:
    if percentage == 0:
      return 0
    if not (-1 <= percentage <= 1):
      raise ValueError("Percentage must be between -1 and 1")
    return self.twentysix_speed * percentage
    
  def get_thirteen_delta(self, percentage: float) -> float:
    if percentage == 0:
      return 0
    if not (-1 <= percentage <= 1):
      raise ValueError("Percentage must be between -1 and 1")
    return self.thirteen_speed * percentage
