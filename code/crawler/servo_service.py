import RPi.GPIO as GPIO
import time
import time

class ServoService:

    ###############################
    # Servo Notes                 #
    # The center position is 7    #
    # The right position is 12    #
    # The left position is 2      #
    ###############################
    # Forward motion 
    # Left_Servo 8.2
    # Right_Servo 6.6
    ###############################
    # Backward motion
    # Left_Servo TOBEDONE
    # Right_Servo TOBEDONE

    def __init__(self, right_servo_pin = 26, left_servo_pin = 13, right_center_position = 7, left_center_position = 6.9):
        GPIO.cleanup()
        # Set the GPIO mode to BCM
        GPIO.setmode(GPIO.BCM)
        # Define both servo pins as outputs
        self.right_servo_pin = right_servo_pin
        self.left_servo_pin = left_servo_pin
        GPIO.setup(self.right_servo_pin, GPIO.OUT)
        GPIO.setup(self.left_servo_pin, GPIO.OUT)
        # Create PWM objects with a frequency of 50 Hz
        self.right_pwm = GPIO.PWM(self.right_servo_pin, 50)
        self.left_pwm = GPIO.PWM(self.left_servo_pin, 50)
        # bring both pwm into a neutral position
        self.right_center_position = right_center_position
        self.left_center_position = left_center_position
        self.right_pwm.start(self.right_center_position)
        self.left_pwm.start(self.left_center_position)

    def go_left(self, duration = 1):
        # during the duration of 1 second move in the left direction
        self.right_pwm.ChangeDutyCycle(self.right_center_position - 0.6)
        self.left_pwm.ChangeDutyCycle(self.left_center_position + 1.3)
        time.sleep(duration)        

    def go_right(self, duration = 1):
        # during the duration of 1 second move in the right direction
        self.right_pwm.ChangeDutyCycle(self.right_center_position - 0.2)
        self.left_pwm.ChangeDutyCycle(self.left_center_position + 1.6)
        time.sleep(duration)

    def stop(self, duration = 1):
        # bring both pwm into a neutral position
        self.right_pwm.ChangeDutyCycle(self.right_center_position)
        self.left_pwm.ChangeDutyCycle(self.left_center_position)
        time.sleep(duration)

    def go_forward(self, duration = 1):
        # bring both pwm into a neutral forward position
        print("Moving forward, at 6.6 and 8.2")
        self.right_pwm.ChangeDutyCycle(self.right_center_position - 0.4)
        self.left_pwm.ChangeDutyCycle(self.left_center_position + 1.3)
        time.sleep(duration)

    def go_backward(self, additional_speed = 1.5, duration = 1):
        # bring both pwm into a neutral backward position
        self.right_pwm.ChangeDutyCycle(self.right_center_position - additional_speed/2)
        self.left_pwm.ChangeDutyCycle(self.left_center_position + additional_speed)
        time.sleep(duration)

    def rotate(self, additional_speed = 3, duration = 1):
        self.right_pwm.ChangeDutyCycle(7 - additional_speed)
        self.left_pwm.ChangeDutyCycle(self.left_center_position)
        time.sleep(duration)

    def go_specific_speed(self, specific_speed, duration):
        self.right_pwm.ChangeDutyCycle(specific_speed)
        self.left_pwm.ChangeDutyCycle(-1 *specific_speed)
        time.sleep(duration)
        
    def go_only_right(self, duration = 1):
        self.right_pwm.ChangeDutyCycle(self.right_center_position + 0.4)
        time.sleep(duration)
        
    def go_only_left(self, duration = 1):
        self.left_pwm.ChangeDutyCycle(self.left_center_position + 0.4)
        time.sleep(duration)

    def rotate_360(self):
        self.rotate(duration=10)

    def close(self):
        self.right_pwm.stop()
        self.left_pwm.stop()
        GPIO.cleanup()
