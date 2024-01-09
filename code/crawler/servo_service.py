import RPi.GPIO as GPIO
import time

# Set the GPIO mode and specify the pin number
servo_pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object with a frequency of 50Hz
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_speed(speed):
    # Map speed from -100 to 100 to a duty cycle between 2 and 12
    duty_cycle = 2 + (speed / 100) * 10
    pwm.ChangeDutyCycle(duty_cycle)

try:
    while True:
        # Move the servo in one direction (clockwise)
        set_speed(-20)  # You can adjust the speed if needed
        time.sleep(1)

except KeyboardInterrupt:
    # Stop the servo on Ctrl+C
    set_speed(0)
    pwm.stop()
    GPIO.cleanup()
