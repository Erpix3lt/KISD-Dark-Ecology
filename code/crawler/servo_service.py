import RPi.GPIO as GPIO
import time
import logging
import time

class ServoService:

    def __init__(self, right_servo_pin = 26, left_servo_pin = 13, start_position = 7.5):
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
        self.right_pwm.start(start_position)
        self.left_pwm.start(start_position)
        logging.debug("Initialised ServoService with the following values: right_servo_pin: %d, left_servo_pin: %d", self.right_servo_pin, self.left_servo_pin)

    def go_left(self, additional_speed = 5, curve_steepness = 2,  duration = 1):
        # during the duration of 1 second move in the left direction
        logging.debug("Moving left with additional_speed: %d, curve_steepness: %d and duration: %d", additional_speed, curve_steepness, duration)
        self.right_pwm.ChangeDutyCycle(7.5 + additional_speed)
        self.left_pwm.ChangeDutyCycle(7.5 + (additional_speed / curve_steepness))
        time.sleep(duration)
        # bring both pwm into a neutral position
        logging.debug("Bringing both pwm into a neutral position")
        self.right_pwm.ChangeDutyCycle(7.5)
        self.left_pwm.ChangeDutyCycle(7.5)

    def go_right(self, additional_speed = 5, curve_steepness = 2, duration = 1):
        # during the duration of 1 second move in the right direction
        logging.debug("Moving right with additional_speed: %d, curve_steepness: %d and duration: %d", additional_speed, curve_steepness, duration)
        self.right_pwm.ChangeDutyCycle(7.5 + (additional_speed / curve_steepness))
        self.left_pwm.ChangeDutyCycle(7.5 + additional_speed)
        time.sleep(duration)
        # bring both pwm into a neutral position
        logging.debug("Bringing both pwm into a neutral position")
        self.right_pwm.ChangeDutyCycle(7.5)
        self.left_pwm.ChangeDutyCycle(7.5)

    def stop(self):
        # bring both pwm into a neutral position
        logging.debug("Stopping, bringing both pwm into a neutral position")
        self.right_pwm.ChangeDutyCycle(7.5)
        self.left_pwm.ChangeDutyCycle(7.5)

    def go_forward(self, additional_speed = 5, duration = 1):
        # bring both pwm into a neutral position
        logging.debug("Moving forward with additional_speed: %d and duration: %d", additional_speed, duration)
        self.right_pwm.ChangeDutyCycle(7.5 + additional_speed)
        self.left_pwm.ChangeDutyCycle(7.5 + additional_speed)
        time.sleep(duration)
        # bring both pwm into a neutral position
        logging.debug("Bringing both pwm into a neutral position")
        self.right_pwm.ChangeDutyCycle(7.5)
        self.left_pwm.ChangeDutyCycle(7.5)

    def go_backward(self, additional_speed = 5, duration = 1):
        # bring both pwm into a neutral position
        logging.debug("Moving backward with additional_speed: %d and duration: %d", additional_speed, duration)
        self.right_pwm.ChangeDutyCycle(7.5 - additional_speed)
        self.left_pwm.ChangeDutyCycle(7.5 - additional_speed)
        time.sleep(duration)
        # bring both pwm into a neutral position
        logging.debug("Bringing both pwm into a neutral position")
        self.right_pwm.ChangeDutyCycle(7.5)
        self.left_pwm.ChangeDutyCycle(7.5)

    def rotate(self, additional_speed = 5, duration = 1):
        #implementation of a rotation
        logging.debug("Rotating with additional_speed: %d and duration: %d", additional_speed, duration)
        self.right_pwm.ChangeDutyCycle(7.5 - additional_speed)
        self.left_pwm.ChangeDutyCycle(7.5 + additional_speed)
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

servoService = ServoService()

while True:
    servoService.go_backward()
    time.sleep(2)
