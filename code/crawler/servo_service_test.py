from servo_service import ServoService

servoService = ServoService()

while True:
    print("going forward for 5 steps")
    servoService.go_forward()
    print("Finished going forward for 5 steps")
    print("going backward for 5 steps")
    servoService.go_backward()
    print("Finished going backward for 5 steps")
    print("going left for 5 steps")
    servoService.go_left()
    print("Finished going left for 5 steps")
    print("going right for 5 steps")
    servoService.go_right()
    print("Finished going right for 5 steps")
    print("stopping for 10 second")
    servoService.stop(10)

