from servo_service import ServoService

servoService = ServoService()

while True:
    direction = input("Enter direction (F for Forward, B for Backward, R for Right, L for Left, Q to Quit): ").upper()

    if direction == 'F':
        print("Going Forward")
        servoService.go_forward(duration=2)
    elif direction == 'B':
        print("Going Backward")
        servoService.go_backward(duration=2)
    elif direction == 'R':
        print("Going Right")
        servoService.go_right(duration=2)
    elif direction == 'L':
        print("Going Left")
        servoService.go_left(duration=2)
    elif direction == 'Q':
        print("Quitting")
        break
    else:
        print("Invalid input. Please enter F, B, R, L, or Q.")
