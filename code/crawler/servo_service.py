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

    def __init__(self, pin_twentysix = 26, pin_thirteen = 13, twentysix_center_position = 7, thirteen_center_position = 7.1):
        GPIO.cleanup()
        # Set the GPIO mode to BCM
        GPIO.setmode(GPIO.BCM)
        # Define both servo pins as outputs
        self.pin_twentysix = pin_twentysix
        self.pin_thirteen = pin_thirteen
        GPIO.setup(self.pin_twentysix, GPIO.OUT)
        GPIO.setup(self.pin_thirteen, GPIO.OUT)
        # Create PWM objects with a frequency of 50 Hz
        self.twentysix_pwm = GPIO.PWM(self.pin_twentysix, 50)
        self.thirteen_pwm = GPIO.PWM(self.pin_thirteen, 50)
        # bring both pwm into a neutral position
        self.twentysix_center_position = twentysix_center_position
        self.thirteen_center_position = thirteen_center_position
        self.twentysix_pwm.start(self.twentysix_center_position)
        self.thirteen_pwm.start(self.thirteen_center_position)

    def go_left(self, duration = 1):
        # during the duration of 1 second move in the left direction
        self.twentysix_pwm.ChangeDutyCycle(self.twentysix_center_position - 0.6)
        self.thirteen_pwm.ChangeDutyCycle(self.thirteen_center_position + 1.3)
        time.sleep(duration)        

    def go_right(self, duration = 1):
        # during the duration of 1 second move in the right direction
        self.twentysix_pwm.ChangeDutyCycle(self.twentysix_center_position - 1)
        self.thirteen_pwm.ChangeDutyCycle(self.thirteen_center_position + 1.6)
        time.sleep(duration)

    def stop(self, duration = 1):
        # bring both pwm into a neutral position
        self.twentysix_pwm.ChangeDutyCycle(self.twentysix_center_position)
        self.thirteen_pwm.ChangeDutyCycle(self.thirteen_center_position)
        time.sleep(duration)

    def go_forward(self, duration = 1):
        # bring both pwm into a neutral forward position
        print("Moving forward, at 6.6 and 8.2")
        self.twentysix_pwm.ChangeDutyCycle(self.twentysix_center_position - 0.4)
        self.thirteen_pwm.ChangeDutyCycle(self.thirteen_center_position + 1.3)
        time.sleep(duration)

    def go_backward(self, additional_speed = 1.5, duration = 1):
        # bring both pwm into a neutral backward position
        self.twentysix_pwm.ChangeDutyCycle(self.twentysix_center_position - additional_speed/2)
        self.thirteen_pwm.ChangeDutyCycle(self.thirteen_center_position + additional_speed)
        time.sleep(duration)

    def rotate(self, additional_speed = 3, duration = 1):
        self.twentysix_pwm.ChangeDutyCycle(7 - additional_speed)
        self.thirteen_pwm.ChangeDutyCycle(self.thirteen_center_position)
        time.sleep(duration)

    def go_specific_speed(self, specific_speed, duration):
        self.twentysix_pwm.ChangeDutyCycle(specific_speed)
        self.thirteen_pwm.ChangeDutyCycle(-1 *specific_speed)
        time.sleep(duration)
        
    def go_only_right(self, duration = 1):
        self.twentysix_pwm.ChangeDutyCycle(self.twentysix_center_position - 3.5)
        time.sleep(duration)
        
    def go_only_left(self, duration = 1):
        self.thirteen_pwm.ChangeDutyCycle(self.thirteen_center_position + 1.5)
        time.sleep(duration)

    def rotate_360(self):
        self.rotate(duration=10)

    def close(self):
        self.twentysix_pwm.stop()
        self.thirteen_pwm.stop()
        GPIO.cleanup()
