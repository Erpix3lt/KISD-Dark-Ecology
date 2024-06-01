import RPi.GPIO as GPIO

class ServoService:

    def __init__(self, pin_twentysix = 26, pin_thirteen = 13, twentysix_center_position = 7, thirteen_center_position = 7.1):
        GPIO.cleanup()
        # Set the GPIO mode to BCM
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_twentysix, GPIO.OUT)
        GPIO.setup(pin_thirteen, GPIO.OUT)
        # Create PWM objects with a frequency of 50 Hz
        self.twentysix_pwm = GPIO.PWM(pin_twentysix, 50)
        self.thirteen_pwm = GPIO.PWM(pin_thirteen, 50)
        # bring both pwm into a neutral position
        self.twentysix_center_position = twentysix_center_position
        self.thirteen_center_position = thirteen_center_position
        self.twentysix_pwm.start(self.twentysix_center_position)
        self.thirteen_pwm.start(self.thirteen_center_position)
        
    def set_motor_speed(self, twentysix_delta: int, thirteen_delta: int):
        """
        Sets the speed of the servo motors by adjusting their duty cycles.

        Args:
            twentysix_delta (int): Change in duty cycle for the first servo motor.
            thirteen_delta (int): Change in duty cycle for the second servo motor.
        """
        self.twentysix_pwm.ChangeDutyCycle(self.twentysix_center_position + twentysix_delta)
        self.thirteen_pwm.ChangeDutyCycle(self.thirteen_center_position + thirteen_delta)

    def stop(self):
        """
        Stops the servo motors by resetting their duty cycles to the center position.
        """
        self.twentysix_pwm.ChangeDutyCycle(self.twentysix_center_position)
        self.thirteen_pwm.ChangeDutyCycle(self.thirteen_center_position)

    def close(self):
        """
        Stops the PWM signals and performs GPIO cleanup.
        """
        self.twentysix_pwm.stop()
        self.thirteen_pwm.stop()
        GPIO.cleanup()