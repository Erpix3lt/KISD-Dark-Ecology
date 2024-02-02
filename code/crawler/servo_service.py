import RPi.GPIO as GPIO
import time
import logging

class ServoService:

    ###############################
    # Servo Notes                 #
    # The center position is 7    #
    # The right position is 12    #
    # The left position is 2      #
    ###############################

    def __init__(self, right_servo_pin = 26, left_servo_pin = 13):
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
        # Values for the center position of the servos
        self.right_servo_center = 7
        self.left_servo_center = 6.9
        # Additional Speed Control
        self.additional_speed = 3
        # bring both pwm into a neutral position
        self.right_pwm.start(self.right_servo_center)
        self.left_pwm.start(self.left_servo_center)
        logging.debug("Initialised ServoService with the following values: right_servo_pin: %d, left_servo_pin: %d", self.right_servo_pin, self.left_servo_pin)

    ###############################
    # Advanced Movement Control   #
    ###############################
        
    def go_forward(self, steps= 5):
        logging.debug("Moving forward with additional_speed: %d and steps: %d", self.additional_speed, steps)
        for _ in range(steps):
            self.rotate_left_servo_once(duration=2.5)
            self.rotate_right_servo_once(duration=2.5)

    def go_backward(self, steps= 5):
        logging.debug("Moving backward with additional_speed: %d and steps: %d", self.additional_speed, steps)
        for _ in range(steps):
            self.rotate_right_servo_backwards_once(0.5)
            self.rotate_left_servo_backwards_once(0.5)

    def go_left(self, steps= 5):
        logging.debug("Moving left with additional_speed: %d and steps: %d", self.additional_speed, steps)
        for step in range(steps):
            self.rotate_right_servo_once()
            # move every second step right servo
            if step % 2 == 0:
                self.rotate_left_servo_once()

    def go_right(self, steps= 5):
        logging.debug("Moving right with additional_speed: %d and steps: %d", self.additional_speed, steps)
        for step in range(steps):
            self.rotate_left_servo_once()
            # move every second step left servo
            if step % 2 == 0:
                self.rotate_right_servo_once()

    ###############################
    # Basic Movement Control      #
    ###############################
                
    def stop(self, duration = 1, right_servo_center_custom = None, left_servo_center_custom = None):
        if right_servo_center_custom is None:
            right_servo_center_custom = self.right_servo_center
        if left_servo_center_custom is None:
            left_servo_center_custom = self.left_servo_center
        # bring both pwm into a neutral position
        logging.debug("Stopping, bringing both pwm into a neutral position")
        self.right_pwm.ChangeDutyCycle(right_servo_center_custom)
        self.left_pwm.ChangeDutyCycle(left_servo_center_custom)
        time.sleep(duration)

    #TODO Modify values to fit 360 degree rotation
    def spin_360_right(self, duration = 10):
        #implementation of a 360 degree rotation
        logging.debug("Rotating 360 degrees")
        self.rotate_right_servo(self.additional_speed, duration)

    def spin_360_left(self, duration = 10):
        #implementation of a 360 degree rotation
        logging.debug("Rotating 360 degrees")
        self.rotate_left_servo(self.additional_speed, duration)

    def spin_left(self, duration):
        #implementation of a 360 degree rotation
        logging.debug("Rotating left")
        self.rotate_left_servo(self.additional_speed, duration)
    
    def spin_right(self, duration):
        #implementation of a 360 degree rotation
        logging.debug("Rotating right")
        self.rotate_right_servo(self.additional_speed, duration)

    def rotate_right_servo_once(self, duration = 1.46):
        self.rotate_right_servo(self.additional_speed, duration)

    def rotate_left_servo_once(self, duration = 1.43):
        self.rotate_left_servo(self.additional_speed, duration)

    def rotate_left_servo_backwards_once(self, duration = 0.2):
        print("going backwards, with duration: ", duration)
        self.rotate_left_servo(-1* (self.additional_speed), duration)

    def rotate_right_servo_backwards_once(self, duration = 0.2):
        print("going backwards, with duration: ", duration)
        self.rotate_right_servo(-1* (self.additional_speed), duration)

    def rotate_right_servo(self, additional_speed, duration):
        self.right_pwm.ChangeDutyCycle(self.right_servo_center + additional_speed)
        time.sleep(duration)
        self.stop(0)

    def rotate_left_servo(self, additional_speed, duration):
        self.left_pwm.ChangeDutyCycle(self.left_servo_center - additional_speed)
        time.sleep(duration)
        self.stop(0)


    def close(self):
        # Clean up GPIO on program exit
        self.right_pwm.stop()
        self.left_pwm.stop()
        GPIO.cleanup()

