import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from servo_service import ServoService

servoService = ServoService()

print("going forward")
servoService.go_forward(duration=5)
print("going backward")
servoService.stop(1)
servoService.go_backward(duration=5)
print("going left")
servoService.stop(1)
servoService.go_left(duration=10)
print("going right")
servoService.stop(1)
servoService.go_right(duration=10)
print("going only left")
servoService.stop(1)
servoService.go_only_left(duration=5)
print("going only right")
servoService.stop(1)
servoService.go_only_right(duration=5)
print("rotating")
servoService.stop(1)
servoService.rotate(duration=5)
print("stopping")
servoService.stop(duration=5)
print("rotating 360")
servoService.stop(1)
servoService.rotate_360()

