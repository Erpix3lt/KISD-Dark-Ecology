from servo_service import ServoService

servoService = ServoService()


print("rotating for 3.5 seconds")
servoService.rotate_left_servo_once()
