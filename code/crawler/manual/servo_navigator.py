import os
import sys
import curses
from threading import Thread, Event

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from servo_service import ServoService

servoService = ServoService()

# Flags to indicate whether a key is pressed
stop_event = Event()
direction_event = Event()

current_direction = None

def control_servo():
    global current_direction
    while not stop_event.is_set():
        if direction_event.is_set():
            if current_direction == 'F':
                print("Going Forward")
                servoService.go_forward()
            elif current_direction == 'B':
                print("Going Backward")
                servoService.go_backward()
            elif current_direction == 'L':
                print("Going Left")
                servoService.go_left()
            elif current_direction == 'R':
                print("Going Right")
                servoService.go_right()
        else:
            servoService.stop()

def main(stdscr):
    global current_direction

    # Clear screen
    stdscr.clear()

    # Non-blocking input
    stdscr.nodelay(True)

    # Loop until user presses 'q'
    while True:
        key = stdscr.getch()

        if key == ord('q'):
            stop_event.set()
            break

        if key == ord('w'):
            current_direction = 'F'
            direction_event.set()
        elif key == ord('s'):
            current_direction = 'B'
            direction_event.set()
        elif key == ord('a'):
            current_direction = 'L'
            direction_event.set()
        elif key == ord('d'):
            current_direction = 'R'
            direction_event.set()
        else:
            direction_event.clear()
            servoService.stop()

# Start control loop in a separate thread
control_thread = Thread(target=control_servo)
control_thread.start()

# Initialize curses
curses.wrapper(main)

# Wait for the control thread to finish
control_thread.join()
