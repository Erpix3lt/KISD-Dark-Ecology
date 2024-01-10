import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the servo
servo_pin = 26

# Set up the GPIO pin for output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object with a frequency of 50 Hz
pwm = GPIO.PWM(servo_pin, 50)

# Start PWM with a duty cycle of 7.5% (neutral position for most servos)
pwm.start(7.5)

try:
    print("Servo is moving. Press Ctrl+C to stop.")
    
    # Run the servo continuously in one direction
    while True:
        # You can adjust the duty cycle to control the speed and direction
        # For continuous rotation servos, values below 7.5% move in one direction,
        # and values above 7.5% move in the opposite direction.
        # Experiment with the values to find the desired speed.
        pwm.ChangeDutyCycle(10)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping servo movement.")

finally:
    # Clean up GPIO on program exit
    pwm.stop()
    GPIO.cleanup()