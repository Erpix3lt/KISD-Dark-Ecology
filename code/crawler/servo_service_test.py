from servo_service import ServoService

servoService = ServoService()

while True:
    print("rotating for 3.5 seconds")
    servoService.rotate_left_servo_once()
   