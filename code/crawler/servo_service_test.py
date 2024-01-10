from servo_service import ServoService
import logging

class ServoServiceTest():

    def __init__(self):
        self.servo_service = ServoService()

servo_service_test = ServoServiceTest()

logging.warn("Running go_left() test")
