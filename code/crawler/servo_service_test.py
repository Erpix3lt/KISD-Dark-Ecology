from servo_service import ServoService

servoService = ServoService()

while True:
    print("going forward")
    servoService.go_forward(duration=30)
    # print("going backward")
    # servoService.go_backward(duration=5)
    # print("going left")
    # servoService.go_left(duration=5)
    # print("going right")
    # servoService.go_right(duration=5)
    # print("rotating")
    # servoService.rotate(duration=5)
    # print("stopping")
    # servoService.stop(duration=5)
    # print("rotating 360")
    # servoService.rotate_360()
    
