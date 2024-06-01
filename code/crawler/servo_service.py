import RPi.GPIO as GPIO

class ServoService:

    def __init__(self, pin_twentysix = 26, pin_thirteen = 13, twentysix_center_position = 7, thirteen_center_position = 7.1):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_twentysix, GPIO.OUT)
        GPIO.setup(pin_thirteen, GPIO.OUT)
        self.twentysix_pwm = GPIO.PWM(pin_twentysix, 50)
        self.thirteen_pwm = GPIO.PWM(pin_thirteen, 50)
        
        self.twentysix_center_position = twentysix_center_position
        self.thirteen_center_position = thirteen_center_position
        self.twentysix_pwm.start(self.twentysix_center_position)
        self.thirteen_pwm.start(self.thirteen_center_position)
        
    def set_motor_speed(self, twentysix_delta: float, thirteen_delta: float):
        """
        Sets the speed of the servo motors by adjusting their duty cycles.

        Args:
            twentysix_delta (int): Change in duty cycle for the first servo motor.
            thirteen_delta (int): Change in duty cycle for the second servo motor.
        """
        print(f'Set motor speed with values, twentysix_delta: {twentysix_delta} and thirteen_delta {thirteen_delta}')
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