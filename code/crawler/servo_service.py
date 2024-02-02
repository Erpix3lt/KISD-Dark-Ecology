import RPi.GPIO as GPIO
import time
import logging
import time

class ServoService:

    ###############################
    # Servo Notes                 #
    # The center position is 7    #
    # The right position is 12    #
    # The left position is 2      #
    ###############################

    def __init__(self, right_servo_pin = 26, left_servo_pin = 13, center_position = 7):
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
        self.right_pwm.start(center_position)
        self.left_pwm.start(center_position)
        logging.debug("Initialised ServoService with the following values: right_servo_pin: %d, left_servo_pin: %d", self.right_servo_pin, self.left_servo_pin)

    def go_left(self, additional_speed = 3, curve_steepness = 0.5,  duration = 1):
        # during the duration of 1 second move in the left direction
        logging.debug("Moving left with additional_speed: %d, curve_steepness: %d and duration: %d", additional_speed, curve_steepness, duration)
        self.right_pwm.ChangeDutyCycle(7 + additional_speed)
        self.left_pwm.ChangeDutyCycle(7 + curve_steepness)
        time.sleep(duration)        

    def go_right(self, additional_speed = 3, curve_steepness = 0.5, duration = 1):
        # during the duration of 1 second move in the right direction
        logging.debug("Moving right with additional_speed: %d, curve_steepness: %d and duration: %d", additional_speed, curve_steepness, duration)
        self.right_pwm.ChangeDutyCycle(7.5 + curve_steepness)
        self.left_pwm.ChangeDutyCycle(7.5 + additional_speed)
        time.sleep(duration)

    def stop(self, duration = 1):
        # bring both pwm into a neutral position
        logging.debug("Stopping, bringing both pwm into a neutral position")
        self.right_pwm.ChangeDutyCycle(7)
        self.left_pwm.ChangeDutyCycle(7)
        time.sleep(duration)

    def go_forward(self, additional_speed = 3, duration = 1):
        # bring both pwm into a neutral forward position
        logging.debug("Moving forward with additional_speed: %d and duration: %d", additional_speed, duration)
        self.right_pwm.ChangeDutyCycle(7 + additional_speed)
        self.left_pwm.ChangeDutyCycle(7 - additional_speed)
        time.sleep(duration)

    def go_backward(self, additional_speed = 1.5, duration = 1):
        # bring both pwm into a neutral backward position
        logging.debug("Moving backward with additional_speed: %d and duration: %d", additional_speed, duration)
        self.right_pwm.ChangeDutyCycle(7 - additional_speed)
        self.left_pwm.ChangeDutyCycle(7 - additional_speed)
        time.sleep(duration)

    def rotate(self, additional_speed = 3, duration = 1):
        logging.debug("Rotating with additional_speed: %d and duration: %d", additional_speed, duration)
        self.right_pwm.ChangeDutyCycle(7 - additional_speed)
        self.left_pwm.ChangeDutyCycle(7 + additional_speed)
        time.sleep(duration)

    def go_specific_speed(self, specific_speed, duration):
        logging.debug("Moving with specific speed: %d and duration %d", specific_speed, duration)
        self.right_pwm.ChangeDutyCycle(specific_speed)
        self.left_pwm.ChangeDutyCycle(specific_speed)
        time.sleep(duration)

    def rotate_360(self):
        #implementation of a 360 degree rotation
        logging.debug("Rotating 360 degrees")
        self.rotate(duration=10)

    def close(self):
        # Clean up GPIO on program exit
        self.right_pwm.stop()
        self.left_pwm.stop()
        GPIO.cleanup()
