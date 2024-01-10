import RPi.GPIO as GPIO
import time

class ServoService:

    def __init__(self):
        # Set the GPIO mode to BCM
        GPIO.setmode(GPIO.BCM)
        # Define both servo pins as outputs
        self.right_servo_pin = 26
        self.left_servo_pin = 13
        GPIO.setup(self.right_servo_pin, GPIO.OUT)
        GPIO.setup(self.left_servo_pin, GPIO.OUT)
        # Create PWM objects with a frequency of 50 Hz
        self.right_pwm = GPIO.PWM(self.right_servo_pin, 50)
        self.left_pwm = GPIO.PWM(self.left_servo_pin, 50)
        # bring both pwm into a neutral position
        self.right_pwm.start(7.5)
        self.left_pwm.start(7.5)

    def go_left(self, speed_difference = 10, duration = 1):
        # during the duration of 1 second move in the left direction
        add_speed = speed_difference / 2
        self.right_pwm.ChangeDutyCycle(7.5 + add_speed)
        self.left_pwm.ChangeDutyCycle(7.5 - add_speed)
        time.sleep(duration)
        # bring both pwm into a neutral position
        self.right_pwm.ChangeDutyCycle(7.5)
        self.left_pwm.ChangeDutyCycle(7.5)

    def go_right(self, speed_difference = 10, duration = 1):
        # during the duration of 1 second move in the right direction
        add_speed = speed_difference / 2
        self.right_pwm.ChangeDutyCycle(7.5 - add_speed)
        self.left_pwm.ChangeDutyCycle(7.5 + add_speed)
        time.sleep(duration)
        # bring both pwm into a neutral position
        self.right_pwm.ChangeDutyCycle(7.5)
        self.left_pwm.ChangeDutyCycle(7.5)

    def stop(self):
        # bring both pwm into a neutral position
        self.right_pwm.ChangeDutyCycle(7.5)
        self.left_pwm.ChangeDutyCycle(7.5)

    def go_forward(self, speed_difference = 10, duration = 1):
        # bring both pwm into a neutral position
        add_speed = speed_difference / 2
        self.right_pwm.ChangeDutyCycle(7.5 + add_speed)
        self.left_pwm.ChangeDutyCycle(7.5 + add_speed)
        time.sleep(duration)
        # bring both pwm into a neutral position
        self.right_pwm.ChangeDutyCycle(7.5)
        self.left_pwm.ChangeDutyCycle(7.5)

    def close(self):
        # Clean up GPIO on program exit
        self.right_pwm.stop()
        self.left_pwm.stop()
        GPIO.cleanup()

