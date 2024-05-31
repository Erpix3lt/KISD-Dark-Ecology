import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from servo_service import ServoService

servoService = ServoService()

while True:
    direction = input("Enter direction (F for Forward, B for Backward, R for Right, L for Left, Q to Quit): ").upper()

    if direction == 'F':
        print("Going Forward")
        servoService.go_forward(duration=1)
    elif direction == 'B':
        print("Going Backward")
        servoService.go_backward(duration=1)
    elif direction == 'OR':
        print("Going O Right")
        servoService.go_only_right(duration=1)
    elif direction == 'R':
        print("Going Right")
        servoService.go_right(duration=1)
    elif direction == 'OL':
        print("Going O LEFT")
        servoService.go_only_left(duration=1)
    elif direction == 'L':
        print("Going Left")
        servoService.go_left(duration=1)
    elif direction == 'Q':
        print("Quitting")
        break
    else:
        print("Invalid input. Please enter F, B, R, L, or Q.")
    servoService.stop(1)
