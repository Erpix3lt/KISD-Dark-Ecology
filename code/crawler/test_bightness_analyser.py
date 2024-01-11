import unittest
import cv2
from brightness_analyser import BrightnessAnalyser
from logger import Logger

class TestBrightnessAnalyser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = Logger()
        cls.analysed_images = []

    @classmethod
    def tearDownClass(cls):
        for analysed_image in cls.analysed_images:
            cls.logger.save_analysed_images_to_web_server(analysed_image)

    def test_process_image_lower_left(self):
        image = cv2.imread('assets/bright_spot_lower_left.jpg')
        analyser = BrightnessAnalyser()
        result, analysed_image = analyser.process_image(image)
        self.analysed_images.append(analysed_image)
        self.assertTrue(result)

    def test_process_image_lower_right(self):
        image = cv2.imread('assets/bright_spot_lower_right.jpg')
        analyser = BrightnessAnalyser()
        result, analysed_image = analyser.process_image(image)
        self.analysed_images.append(analysed_image)
        self.assertFalse(result)

    def test_unprepared_image(self):
        image = cv2.imread('assets/no_bright_spot.jpg')
        analyser = BrightnessAnalyser()
        result, analysed_images = analyser.process_image(image)
        self.analysed_images.append(analysed_images)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
