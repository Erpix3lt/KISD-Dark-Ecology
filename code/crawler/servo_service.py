import RPi.GPIO as GPIO
import time

# Set the GPIO mode and specify the pin number
servo_pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object with a frequency of 50Hz
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_angle(angle):
    duty_cycle = 2 + (angle / 18)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Move the servo to 0 degrees
        set_angle(0)
        time.sleep(1)

        # Move the servo to 90 degrees
        set_angle(90)
        time.sleep(1)

        # Move the servo to 180 degrees
        set_angle(180)
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C
    pwm.stop()
    GPIO.cleanup()
